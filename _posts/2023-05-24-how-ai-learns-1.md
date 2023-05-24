---
title: "How AI Learns, part 1"
date: 2023-01-18T18:45:30-05:00
spec: "how-ai-learns-1"
categories:
  - blog
tags:
  - update
---





1. Introduction
2. History of AI pre-ML
3. ML is learning models to fit data
4. Example: linear regression
    1. Figures
    2. Model parameters
5. What is a model and what is a pdf
    3. Gaussian
        1. Example: heights
        2. Include figures of Gaussians
    4. Gaussian error term
        3. Distribution of values of y if we compared many samples for that x
        4. Figure showing Gaussians on line with data
        5. Zero mean
    5. y=mx+b as p(y|x) (or p(y; x,m,b))
6. Maximum likelihood
    6. We can compute the probability of getting a given set of data if we have a parameterized pdf
    7. Since we already observed the data, want parameters s.t. _It is most likely to be observed_.
    8. Optimize p(x|theta) by varying theta and computing p(x|theta) over all x samples
    9. Can be found analytically for linreg
    10. Corresponds to minimizing least square residuals because they are equal to the negative log-likelihood
7. Gradient descent
    11. Plot of m vs. likelihood
8. Generative modeling
    12. Discriminative vs. generative
    13. This person does not exist
9. Neural networks
    14. Linear vs. non-linear models
    15. Neural network structure
    16. Activation functions
        6. Demonstrate need for nonlinearity with two-layer, two-neuron example
    17. Universal approximation, the brief version
        7. Modeling an underlying joint distribution
        8. Proven for neural networks
        9. Usually designed based on prior work; a lot is known about the ability of different architectures to model different kinds of problems
10. Autoregressive modeling
11. GPT

What does it mean to say that an AI “learned” to do something? Broadly speaking, it means using data to figure out the rules governing what an AI should do in a certain situation.

AI, short for “artificial intelligence”, refers to computer programs which can perform tasks requiring some degree of abstract reasoning. This is a broad class of programs, ranging from simple game-playing algorithms to ChatGPT. The science of AI emerged in the 1950s, as theorists like Alan Turing tried to understand the relation between human problem-solving skills and computer logic. “Intelligence” is a hard concept to define, but one aspect of it is the ability to adapt to new situations. Until the 1980s, this was done by mathematically deriving general rules for finding the solution to a problem of a given format. For example, an AI to solve a Rubik’s cube considers the current arrangement of the cube and makes a move depending on pre-programmed rules that have been shown to be the best. The problem with this approach was that it did not work for more complex problems, like speech recognition. With the end of the Vietnam War in the early 1970s, funding for AI dried up, beginning the period known as the first AI winter. This ended in the early 1980s with the introduction of machine learning, and that’s where our story starts.

The early AI approaches would work for any configuration of a problem, but they required human inventors to first figure out a general means to a solution. This broke down when trying to process language, because the grammatical rules of most languages are far too complicated to write down. Instead, computer scientists realized that they didn’t need to figure out any rules. They just needed to express the input and solution mathematically, and then find the form of a function, or model, that would take the input and give the solution. With enough data, it would then be possible to simply optimize the function to give the most accurate solutions.

You’re probably familiar with an example of this, in finding the line of best fit. This is called linear regression, and it turns out that the underlying math 

  <div id="vis"></div>
  
  <script>
    const spec = "/figures/how-ai-learns-1.vg.json";
  	vegaEmbed("#vis", spec)
    	// result.view provides access to the Vega View API
      .then(result => console.log(result))
      .catch(console.warn);
  </script>

OK, so how do we know how accurate a solution is, and what do these mysterious functions look like? In short, statistics. First, let’s talk about what a _probability distribution_ is. It is a function P(_x_) that describes something observable and tells us _how likely_ it is to observe a value of _x_ relative to all other possible values. We assume that our data is sampled[^1] from an underlying probability distribution. The goal of machine learning is to _learn_ (or “fit” or “train”) a _model _ P(_x_) from data so it best approximates the actual probability distribution of the data.

Let’s consider an example. Suppose we have 100 data points, where each represents the height in centimeters of a certain adult male. We want to model the distribution P(_x_), where _x_ is a height in centimeters. Shown below is a histogram of 500 randomly-sampled heights. Each bar’s width is a range of x-values, and its height is the fraction of our data points that fall into that range. With enough data points, we should be able to assume that that fraction, the density, is _the probability of a man’s height being in that range._ I also plotted the black curve, which is what the histogram will look like if we gathered more data while decreasing the width of each bar.

Male heights are known to follow a normal, or Gaussian, distribution. This is a function of _x_ that has two parameters, 𝜇 and 𝜎, so we can write P(_x_) as P(_x_; 𝜇, 𝜎) to specify this. The black curve in the plot is the actual P(_x_) for the data, which is what we are trying to estimate. We can solve for 𝜇 and 𝜎 using known formulas, because they are the mean and standard deviation of the data respectively, but let’s think about what P(_x_; 𝜇, 𝜎) really means. It is a function telling us how likely it is to find a man with a height of _x_. We have already found 500 men with these heights. The probability that we observed them is 1. Instead, we need to find the 𝜇 and 𝜎 such that _we have the greatest likelihood of having found the data we did_. The likelihood of finding a given _x_ is P(_x_), and because these are independent samples of the same distribution, the total _data likelihood_ is the product of all P(_x<sub>i</sub>_), thus P(data; 𝜇, 𝜎)= P(_x<sub>1</sub>_)* P(_x<sub>2</sub>_)* P(_x<sub>3</sub>_)*...* P(_x<sub>500</sub>_) (𝜇, 𝜎 are also parameters of each P(_x<sub>i</sub>_), but I omitted them for clarity).

This is really important to understand. All machine learning is is optimizing a model such that it would be _most likely_ to give us our observed data if it were equal to the “true” underlying process. 

But how do programmers decide what kind of model to use? A core challenge in machine learning is the _bias-variance tradeoff_: the more closely a model fits a given set of training data (lower _bias_), the worse it will fit other data from the same source (higher _variance_), and vice versa. When a model has as many parameters as the training data has numbers, there is a tendency for the model to get 100% accuracy. This is a problem, because that means the model is overfitted: it has essentially memorized the specific training data, so it is not able to generalize in the real world.

ChatGPT is one of the most complicated AI models in existence, having learned from a massive amount of text. It also learns by minimizing an error over training data, but the error and the training data are a little different. In order to understand them, we’ll first take a step back. ChatGPT built on top of another model called GPT-3, where GPT stands for Generative Pre-trained Transformer. Transformer refers to the type of underlying model, which turns out to be a function with 175 billion parameters. Generative pre-training is the means by which GPT-3 learns. With generative pre-training, there are two kinds of inputs, and the training data has both. The first kind is next-token prediction, in which the model is given a sequence of words (tokens)


<!-- Footnotes themselves at the bottom. -->
## Notes

[^1]:
     Sampling in this context means randomly chosen _x_ such that with enough samples, the fraction of samples equal to _x_ approaches P(_x_).
