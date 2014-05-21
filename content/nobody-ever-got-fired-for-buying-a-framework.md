Title: Nobody ever got fired for buying a framework
Date: 2014-05-20 12:00
Author: Johannes Seitz
Category: Persistency
Tags: risk mitigation, frameworks
Slug: nobody-ever-got-fired-for-buying-a-framework

Today James Shore struck a nerve with me when he tweeted:

<blockquote class="twitter-tweet" lang="en"><p>When did &quot;use a framework&quot; become a substitute for knowing how to design? And why did designing code become &quot;you&#39;re writing a framework?&quot;</p>&mdash; James Shore (@jamesshore) <a href="https://twitter.com/jamesshore/statuses/468528056533913601">May 19, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

However, the question on my mind is not so much **when** people started using frameworks as a substitute for good design. I am more interested in the **why**? 

In my carreer as a software developer I've been working with frameworks quite a lot. That is when I came to hypothesise about the incentives that shape the adoption of frameworks and also the hidden drawbacks of framework reliance. 

This article explains the reasons I think businesses choose to buy into frameworks in a big way. The next article will explain why I feel some developers cling to their frameworks.

## Advantages to the business 

So why do businesses buy into framworks? My hypothesis: it's mostly **risk mitigation**. 

### Risk mitigation

Software projects still come with lots of risk from a business perspective. And the scariest of all just might be a failed project. No return on investment. We spent millions of dollars on softare and we got nothing out of it.

Buying a framework ensures the business that some basic core functionality is already working. Why would anyone build his/her own content management system, e-commerce platform or CRM system when you can just buy the working thing from the industry-leading manufacturer and tinker with it?

There's this list of Fortune 500 companies on the website of then vendor. If it's good enough for them, it ought to be good enough for anyone.

### Let's call in the experts

Now we are talking serious risk mitigation: There are agencies that do nothing but extend frameworks for their customers. Not only do we not need to build this software and risk failure, we can also get a scapegoat to blame when something goes wrong with the customisation! 

And even when we decide to do the project ourselves, the vendor offers workshops that make sure any average programmer can get productive with the framework in no time. If they run into trouble or don't know how to do something we might have to pay someone from the vendor for help, but that's still cheaper than someone who needs to be trained in object-oriented design principles. Do you know how long that takes?

### And we're already half-way done!

Of course most of the core functionality is already part of the framework. So we're already half-way done with the project. All we need to do is take the framework make it look like it's our own. There's just a few cases where the framework does not fit our business. But even in these cases we can probably re-use parts of the framework to speed us up. Sweet!

## Overlooked drawbacks

All these arguments appeal to managers. Especially non-technical managers. The over-arching theme is: risk mitigation. What non-technical managers do not see, is the overlooked cost of frameworks, especially when they come in the guise of products that you adapt

### Serious limitations

Every framework comes with a certain set of design choices already made. There's nothing inherently wrong with that, but it will restraint the possiblities of any product that is built upon this framework. Good frameworks come with modularity and allow for developers to swap out parts that do not match their needs. 

But some things are not easily changed. When the framework is missing hooks and interfaces to customise or replace parts of the system, developers are restrained by the framework. I suppose that is where the common saying amongst developers that "Frameworks make 80% of the work incredibly easy and 20% impossible" comes from.

Of course there may be way to work around these limitations. Hacking the framework, which esentially comes down to misusing it intentionally in order to get around limitations has made for the most brittle and cumbersome solutions to these limitations I have seen in practice. Suffice it to say, this is a maintenance nightmare, translating into high long term costs.

As an example, when the framework dictates a CRUD based approach to everything, because it generates most of the behaviour from declarative descriptions of entities, user interfaces are bound to end up closely reflecting data structures. These frameworks do generally not allow for what [the DDD community came to call a "Task-Based UI"](https://cqrs.wordpress.com/documents/task-based-ui/). The CRUD based UI revolves around data structures and does not reveal how these data structures inter-relate and certainly not around what the user is trying to accomplish.

### What's your competitive advantage?

There is another corollary to the limitations explained in the previous section. When everyone in the industry is using the same standard software to build upon, gaining a competitive edge is really hard. That is especially true when it comes to businesses making most of their money online or moving online at a rapid pace like the music and news content industry. 

What would happen if the iTunes media store or Amazon was just another online shop, hosted on the shoulders of a framework? It's unimaginable. These companies build their own ecosystems and dominate them with innovation at such a large scale that any attempt to build these businesses on anyhting but custom software would surely end up with a fowl compromise or complete failure to do so.

### All grunt work and no play make Jake a dull boy

As a developer, working with a framework can be pretty dull sometimes. When you are just solving the same problems in slight variation over and over again, you are bound to get bored. At least that is I felt working with these frameworks. The most interesting things happen when you break out of the framework sandbox. When you devise hacks that trick the system or just completly decouple yourself and do your own thing.

From a business point of view that's an advantage, because all you need to do is hire average developers with high tolerance for repetitive work. These are the buerocrats of the software development world, who actually enjoy this kind of dull grunt work, because you rarely need to think for yourself. 

### To be continued

We will continue with my observations of the framework developer in the next article, which I will post in the upcoming days. I may even post a third article with my process for evaluating frameworks and measures to partially protect projects from framework lock-in effects and gracefully recover from bad framework choices.
