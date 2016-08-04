---
layout: post
title: Constituencies, First-Past-the-Post and Minority Rule
tags: voting
---

The other day, I rewatched CGP Grey's [excellent videos](https://www.youtube.com/playlist?list=PL9936C719FF689E7D) about the Electoral College. In
[one video](https://youtu.be/7wC42HgLA4k?list=PL9936C719FF689E7D&t=259), Grey shows how it is possible to become President with only about
23% of the popular vote. The UK's constituency-based system shares some key features with the Electoral College, so I wondered whether a similar
feat might be possible here. A quick search for data and a few lines of code later, I had my answer.

First, a primer on UK general elections. The [data](http://www.electoralcommission.org.uk/our-work/our-research/electoral-data) I used was for the 2015 General Election. In this election,
there were 650 constituencies making up the UK. During an election, each of these elects one MP to a seat in Parliament using a [first-past-the-post](https://en.wikipedia.org/wiki/First-past-the-post_voting) voting system. Then, by
[constitutional convention](https://en.wikipedia.org/wiki/Constitutional_convention_(political_custom)), the Queen appoints the leader of the party with a majority of the seats
as Prime Minister and they form the Government. Since MPs are elected using a plurality system, it is common for them to be elected with less than 50% of the vote. For simplicity, I'll assume
a strict two-party system in my analysis, meaning that winning requires a majority of the vote. It's a *wildly* inaccurate assumption, but I'll get back to that.

Hopefully it is clear from the above that the 'winning party' is not necessarily the one that won the most votes, but the one that one that won the most *constituencies*. Despite efforts to equalise the populations of constituencies, these vary dramatically for historical and geographical reasons. For example, in 2015, the [Isle of Wight](https://en.wikipedia.org/wiki/Isle_of_Wight) had an electorate of over 100,000 people. At the other end of the scale, [Na h-Eileanan an Iar](https://en.wikipedia.org/wiki/Na_h-Eileanan_an_Iar_(UK_Parliament_constituency)) had an electorate of only about 22,000 people. This variation means that some votes effectively matter more than others. It also makes the constituency system vulnerable to the same trick that Grey pulled in his video.

In order to gain control of the Government (without coalition), a party must win 326 seats in Parliament. By just barely winning the 326 smallest constituencies, they could win these seats with fewest possible votes. When I analysed the data, I found that this tactic could lead to a party being in government with a startlingly low percentage of the votes overall. Even assuming that everyone votes, less than 23% of the popular vote will get you into government.

|                                         | Minimum total number of votes for 326 seats | Percentage of electorate |
|-----------------------------------------|---------------------------------------------|--------------------------|
| **Assuming 100% turnout**               | 10,646,336                                  | 22.97                    |
| **Using 2015 General Election turnout** | 6,791,227                                   | 14.65                    |

 This compaign strategy is not a realistic one, but the fact that it is even *possible* to win a two-party election with such a small proportion of the votes is
 worrying. If we add realism by removing the two-party restriction then things can only get worse, since first-past-the-post then allows for seats to be won with less than 50% of the votes. The [issues with first-past-the-post](http://www.electoral-reform.org.uk/first-past-the-post) itself are beyond the scope of this post.

 There you have it. The vast range of constituency sizes makes it theoretically possible to win a majority of parliamentary seats with a shockingly small percentage of the popular vote. For those of us who care about the representativeness of our democracy, it is therefore tempting to demand perfect equalisation. We must be careful though. Constituencies are about more than electorate size, so we can't just go chopping and changing them willy-nilly. For more about constituency boundary reform, see the [Electoral Reform Society website](http://www.electoral-reform.org.uk/boundary-reform).

The code used for my analysis is [here]({{site.url}}/assets/Constituencies,%20First%20Past%20the%20Post%20and%20Minority%20Rule/analysis.py) and the exact data is 
[here]({{site.url}}/assets/Constituencies,%20First%20Past%20the%20Post%20and%20Minority%20Rule/Constituencies%20size%20-%20GE%202015.csv).
