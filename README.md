# 🏎 Car Data Visualization

An in depth look at the relationship between the number of gears a car has and its combined MPG rating.

_This is a lab assignment that forms a part of a Machine Learning class at UY._

>This lab is based and uses the 2019 model-year vehicle dataset.

Built in 🐍 Python with `seaborn`, `pandas`, `matplotlib`, and `numpy`.

### __Lab:__

Lets start by looking at all of the graphs generated with the data and what each one represents.

#### __Scatter Plot__

<img src="https://i.ibb.co/bJD20Rv/4.png" height="250" />

An interesting thing to note is that scatter plots create columns when the x axis is ordinal (like number of gears). We can see from the graphs that the cars with one gear have a high MPG. In the other case, cars from gear range 5 to 10 tend to be concentrated a lower MPH. This said, there are cars with 6 gears that do have a high MPH.

#### __Linear Regression Plot__

<img src="https://i.ibb.co/CVqq1Mh/3.png" height="250" />

The Linear Regression plot is supposed to show some sort of trend in the data. However, this just makes it more apparent that the data has no trend. 

#### __Joint Plot__

<img src="https://i.ibb.co/0fYVrZb/2.png" height="250" />

What is nice about this plot is that it allows you to see where the data is condensed in for each axis. Here, it is clear that most of the cars have a MPG of between 20-30. We can also see that the most common number of gears is between 6-8.

#### __Box & Whisker Plot__

<img src="https://i.ibb.co/gb1bBj8/1.png" height="250" />

The Box & Whisker plot allows you to see the concentration of the data and the range of the data. It also allows to see outliers which is interesting. By looking at this data, you can see how the cars with 1 gear are actually more fuel efficient than all the others. Not only do the cars with one gear have a higher MPG, they also have a lower overall range of data. Also note that almost every outlier was increasing in MPG and not decreasing. Then, from 5 to 8, things stay pretty stagnant. However, when you reach 9 and 10, the MPG is lower than the others and also has a low range meaning that the data is generally condensed in that low MPG area.

#### __Swarm Plot__

<img src="https://i.ibb.co/Z1fwGbD/5.png" height="250" />

The swarm plot is even better at displaying this data. It shows how the cars with a lower # of gears actually do have a higher MPG than those with a higher # of gears.

#### __Conclusion:__

Since this data is measuring the car models and not individual cars, you could argue that these models are outliers. However, each model is built differently and manufactured differently. It could very well be argued that there are cars with an incredible efficiency and happen to have 6 or 8 gears. However, just by looking at the data itself, the cars that have a lower number of gears have a higher MPG than those with a higher number of gears (even if it seems counter intuitive).


Built with ❤️ by [@markmusic2727](https://twitter.com/MarkMusic2727).
