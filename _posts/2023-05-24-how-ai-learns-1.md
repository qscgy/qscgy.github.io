---
title: "How AI Learns, part 1"
date: 2023-01-18T18:45:30-05:00
spec: "how-ai-learns-1"
categories:
  - blog
tags:
  - update
---

What does it mean to say that an AI “learned” to do something? Broadly speaking, it means using data to figure out the rules governing what an AI should do in a certain situation.

AI, short for “artificial intelligence”, refers to computer programs which can perform tasks requiring some degree of abstract reasoning. This is a broad class of programs, ranging from simple game-playing algorithms to ChatGPT. The science of AI emerged in the 1950s, as theorists like Alan Turing tried to understand the relation between human problem-solving skills and computer logic. “Intelligence” is a hard concept to define, but one aspect of it is the ability to adapt to new situations. Until the 1980s, this was done by mathematically deriving general rules for finding the solution to a problem of a given format. For example, an AI to solve a Rubik’s cube considers the current arrangement of the cube and makes a move depending on pre-programmed rules that have been shown to be the best. The problem with this approach was that it did not work for more complex problems, like speech recognition. With the end of the Vietnam War in the early 1970s, funding for AI dried up, beginning the period known as the first AI winter. This ended in the early 1980s with the introduction of machine learning, and that’s where our story starts.

The early AI approaches would work for any configuration of a problem, but they required human inventors to first figure out a general means to a solution. This broke down when trying to process language, because the grammatical rules of most languages are far too complicated to write down. The solution was to switch from thinking about AI as following pre-programmed rules to AI as solving for some underlying function that produced all of the observed data. With enough data, it should be possible to find the patterns in the data, and from there find a function, called a model, that can _most accurately reproduce_ the training data set. No handcrafted rules, just using statistics to estimate what produced the data and what future data will look like.

You might be familiar with an example of this, in finding the line of best fit. This is called linear regression, and it is one of the simplest forms of machine learning. The line of best fit is a function of the form _ŷ=mx + b_, where _m_ is the slope of the line and _b_ is the y-intercept (where the line crosses the y-axis, i.e., the value of  _ŷ_ when _x_=0). We write _ŷ_ to indicate that it is the predicted value of _y_, which isn’t the same as the _y_ in the data point (_x, y_). _m_ and _b_ are the values that make the error in the model the smallest. What’s the error? In this case, it’s the average of the squared vertical distance from each point to the line at the same _x_. In other words, it is (_ŷ – y_)<sup>2</sup> averaged over all data points, called the _mean squared error_ or MSE.

The example below shows 20 data points of the position of a water molecule moving forward. It has a constant forward velocity perturbed by random fluctuations due to its temperature[^1]. You can adjust the sliders to vary _m_ and _b_; read on once you think you’ve found the line of best fit.

  <div id="lbf"></div>
  
  <script>
    const spec = "/figures/how-ai-learns-1.vg.json";
  	vegaEmbed("#lbf", spec)
    	// result.view provides access to the Vega View API
      .then(result => console.log(result))
      .catch(console.warn);
  </script>

The true velocity is 5, and the particle started at a distance of 10, so the “true” model producing these data points is _y=5x+10_. But we have these random fluctuations, so how can we solve for the best estimates of _m_ and _b_? In short, statistics. First, let’s talk about what a _probability distribution_ is. It is a function p(_x_) that describes something observable and tells us _how likely_ it is to observe a value of _x_ relative to all other possible values. We assume that our data is sampled[^2] from an underlying probability distribution. The goal of machine learning is to _learn_ (or “fit” or “train”) a _model_ p(_x_) from data so it best approximates the actual probability distribution of the data.

Let’s consider an example. Suppose we have 100 data points, where each represents the height in centimeters of a certain adult male. We want to model the distribution p(_x_), where _x_ is a height in centimeters. Shown below is a histogram of 500 randomly-sampled heights. Each bar’s width is a range of x-values, and its height is the fraction of our data points that fall into that range. With enough data points, we should be able to assume that that fraction, the density, is _the probability of a man’s height being in that range._ I also plotted the black curve, which is what the histogram will look like if we gathered more data while decreasing the width of each bar.

<img src="{{ site.url }}{{ site.baseurl }}/figures/normal.png" alt="A plot of a Gaussian distribution overlaid over a histogram of data drawn from it.">

Male heights are known to follow a normal, or Gaussian, distribution. This is a function of _x_ that has two parameters, 𝜇 and 𝜎, so we can write p(_x_) as p(_x_; 𝜇, 𝜎) to specify this. We can also write _p(x)~N_(𝜇, 𝜎), meaning that _p(x)_ is specifically a Gaussian distribution with these parameters.

The black curve in the plot is the actual p(_x_) for the data, which is what we are trying to estimate. We can solve for 𝜇 and 𝜎 using known formulas, because they are the mean and standard deviation of the data respectively, but let’s think about what p(_x_; 𝜇, 𝜎) really means. It is a function telling us how likely it is to find a man with a height of _x_. We have already found 500 men with these heights. The probability that we observed them is 1. Instead, we need to find the 𝜇 and 𝜎 such that _we have the greatest likelihood of having found the data we did_. The likelihood of finding a given _x_ is p(_x_), and because these are independent samples of the same distribution, the total _data likelihood_ is the product of all p(_x<sub>i</sub>_), thus p(data; 𝜇, 𝜎)= p(_x<sub>1</sub>_)* p(_x<sub>2</sub>_)* p(_x<sub>3</sub>_)*...* p(_x<sub>500</sub>_) (𝜇, 𝜎 are also parameters of each p(_x<sub>i</sub>_), but I omitted them for clarity).

As Albert Einstein showed, the random movements of water molecules also follow a Gaussian distribution. It turns out that random fluctuations in almost anything follow a Gaussian, so much so that linear regression is based on the assumption that _y=mx+b+ε_, where _ε_ follows a Gaussian with 𝜇=0. In words, this means that we assume that every observed value of _y_ is a model term, _mx+b_, plus an error term, _ε_. This is important because it means we can write a probability distribution! Instead of just p(x), we actually want p(y &#124;x), which is the likelihood of measuring _y_ as the position at time _x_. This is called a conditional likelihood, and we will use them later to understand ChatGPT. But all it is is a probability distribution p(y) that has 𝜇, 𝜎, <strong>and _x_</strong> as parameters.

For our line of best fit, we can write _p_(_y_ &#124;_x_) ~ _N_(𝜇=_mx+b, 𝜎_). This tells us something very important: for any given value of _x,_ if we repeated this experiment many times, the measured values of _y_ would follow this Gaussian distribution. Essentially, we are solving the same problem as with mens’ heights _for every single x_. That sounds hard, but we already know how to write down the total likelihood of the data, and we have a formula for the likelihood of each data point. We write _p_(_y_ &#124;_x_)=_p_(_y<sub>1</sub>_; 𝜇=_mx<sub>1</sub>+b, 𝜎_)\*_p_(_y<sub>2</sub>; 𝜇=mx<sub>2</sub>+b, 𝜎_)\*_p_(_y<sub>3</sub>; 𝜇=mx<sub>3</sub>+b, 𝜎_)\*...\*_p_(_y<sub>20</sub>; 𝜇=mx<sub>20</sub>+b, 𝜎_). And now it’s the same problem as before; we just have to find the parameters that maximize this likelihood. It turns out that the optimal 𝜎 is a function of _m_ and _b_, so we just need to find the _m_ and _b_ that maximize the data likelihood. This ends up having the same minimum as the mean squared error from before, but showing this requires more math than I want to include. In machine learning, it is usually the case that the math is based on maximizing a data likelihood, but it is actually implemented in code as minimizing some error function that we can show maximizes the data likelihood.

That’s all for part 1. In part 2, I will get more into the kinds of functions that compose state-of-the-art AI models like ChatGPT. We will also learn what kind of probability distributions and data likelihoods are involved in ChatGPT, because working with words instead of numbers means things have to be a bit different.


<!-- Footnotes themselves at the bottom. -->
## Notes

[^1]:
     This is called Brownian motion, and explaining it is one of Albert Einstein’s three major discoveries from 1905.

[^2]:
     Sampling in this context means randomly chosen _x_ such that with enough samples, the fraction of samples equal to _x_ approaches p(_x_).