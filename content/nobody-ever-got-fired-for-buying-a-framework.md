Title: Nobody ever got fired for buying a framework
Date: 2014-05-21 17:00
Author: Johannes Seitz
Category: Essays
Tags: psychology, frameworks
Slug: nobody-ever-got-fired-for-buying-a-framework

Today James Shore struck a nerve with me when he tweeted:

<blockquote class="twitter-tweet" lang="en"><p>When did &quot;use a framework&quot; become a substitute for knowing how to design? And why did designing code become &quot;you&#39;re writing a framework?&quot;</p>&mdash; James Shore (@jamesshore) <a href="https://twitter.com/jamesshore/statuses/468528056533913601">May 19, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

However, the question on my mind is not so much **when** people started using frameworks as a substitute for good design. I am more interested in the **why**? 

In my career as a software developer I've been working with frameworks quite a lot. That is when I came to hypothesise about the incentives that lead to the adoption of frameworks. I also suffered from the often overlooked drawbacks of building upon a framework. 

This essay is the first in a series, explaining my thoughts why businesses choose to buy into frameworks in a big way. The next article in this series will explain why I feel some developers cling too much to their frameworks. The final article in this series will contain my advice for evaluating and choosing frameworks. So let's get started!

## Advantages to the business 

Why do businesses buy into frameworks? My hypothesis: it's mostly **risk mitigation**. 

### Risk mitigation

Software projects still come with lots of risk from a business perspective. And the scariest of all just might be a failed project. No return on investment. We spent millions of dollars on software and we got nothing out of it.

Buying a framework ensures that some core functionality is already working. Why would anyone build his/her own content management system or e-commerce platform or web framework, when you can just get one from an industry-leading vendor and tinker with it? Look, there's a list of Fortune 500 companies on the website of the vendor. If it's good enough for them, it ought to be good enough for anyone. 

Depending on the product the decision to buy may be pretty expensive, but the perceived risk is close to zero. And the return on investment is already high. 

### Let's call in the experts

Now we are talking serious risk mitigation: there are successful agencies that do nothing but extend and customise frameworks for customers. Not only do we not need to build this software and risk failure, we also get an expert to blame when something goes wrong with the customisation! 

And even if we decide to do the project ourselves, the vendor offers workshops that make any average programmer productive with the framework in no time. If they run into trouble or don't know how to do something we might have to pay someone from the vendor for help. But that's still cheaper than training developers in software design principles and the issues of our business domain.

### And we're already half-way done!

Of course most of the core functionality is already part of the framework. So we're already half-way done with the project. All we need to do is take the framework make it look like it's our own. There's just a few cases where the framework does not fit our business. But even in these cases we can try to re-use parts of the framework to speed us up. Sweet!

## Overlooked drawbacks

All these arguments appeal to managers. Especially non-technical managers. The over-arching theme is: risk mitigation. What non-technical managers do not see, are the limitations of these frameworks. Especially when they come in the guise of shiny marketing promises. It's the proven, no-risk Lego toolkit to solve all your problems.

### Serious limitations

Every framework comes with a certain set of design choices already made. That is what makes developers building on frameworks much faster. There's nothing wrong with that, but it will prevent the possibilities of any product built upon this framework. Good frameworks come with modularity and allow for developers to swap out parts that do not match their needs. 

But some things are not easily changed. When the framework is missing hooks and interfaces to customise or replace parts of the system, it prevents possiblities. I suppose that is where the common saying amongst developers that "Frameworks make 80% of the work easy and 20% impossible" comes from.

This happens for example, when the framework dictates a CRUD based approach for user interaction. This approach forces users are to interact only by creating, reading, editing or deleting things. These approaches are popular, because frameworks may generate most of the code from declarative descriptions of entities.  But the one serious drawback of this approach is that user interfaces are bound to reflect the underlying data structures. That is why they do not allow for what [the DDD community came to call a "Task-Based UI"](https://cqrs.wordpress.com/documents/task-based-ui/). A CRUD based UI revolves around data structures. It does not reveal how these data structures inter-relate and certainly not around what the user is trying to accomplish. 

### We can work around that...

Of course there may be a way to work around these limitations. Hacking the framework, which comes down to misusing it intentionally to get around limitations for example. Hacks have made for the most brittle and cumbersome pieces of code I have seen in practice. Suffice it to say, this is a maintenance nightmare, translating into high long term costs.

### What's your competitive advantage?

There is another corollary to the limitations explained in the previous sections. **When everyone in the industry is using the same standard software to build upon, gaining a competitive edge is really hard**. That is especially true when it comes to businesses making most of their money online or moving online at a rapid pace like the music and news content industry.

What would happen if the iTunes media store or Amazon was just another online shop, hosted on the shoulders of a shop framework? It's unimaginable. These companies build their own ecosystems. They dominate markets with constant innovation. Any attempt to build these services on anyhting but custom software would surely end up with fowl compromise or complete failure.

Developing innovative solutions in framework sandboxes can be hard, due to the limitations. If there is no standard way to do something with your framework, you are on your own. And it gets even tougher when you outsource projects to someone else.  You will need to work closely with a talented development team to come up with simple and workable solutions. And when you decided to outsource the product development to someone else, you are not in control. You might even get the frustrating answer that it can't be done. Consider the oportunity cost.

### All grunt work and no play make Jake a dull boy

As a developer, working with a framework can be pretty dull sometimes. When you are solving the same problems in slight variation over and over again, you are bound to get bored. At least that is I felt working with these frameworks. The most interesting things happen when you break out of the framework sandbox. When you devise hacks that trick the system or just completly decouple yourself and do your own thing.

From a business point of view that's an advantage, because all you need to do is hire average developers with high tolerance for repetitive work. These are the buerocrats of the software development world, who actually enjoy this kind of dull grunt work, because you rarely need to think for yourself.

## What should you do?

These are just some of the pros and cons you should consider when you or your company is faced with the old "build or buy" question. I prefer to make my decisions based on careful reasoning and valuation of the given options. But even so I think that "buy" is the still the default for a lot of companies.

We will continue with my observations of the framework developer in an upcoming part 2 of this article. I will subsequently post a third article about my process for evaluating frameworks. I will also introduces measures to (at least partially) protect projects from framework lock-in effects. This may give development teams the ability to gracefully recover from bad framework choices.
