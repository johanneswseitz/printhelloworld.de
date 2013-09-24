Title: Resisting marshmallows is hard. Adopting TDD, too.
Date: 2013-04-10 14:01
Author: joseitz
Category: Psychology
Slug: be-aware-of-hyperbolic-discounting-when-adopting-tdd

We are not as rational as we think we are. Or as Dan Ariley might put
it: [We're All Predictably Irrational][]. The other day I read "Die
Kunst des klaren Denkens" (lit: The art of clear thinking) by Swiss
author Rolf Dobelli. One of the common logical fallacies Dobelli	
describes in this book is the fallacy of [Hyperbolic Discounting][] -
the inclination to value immediate rewards over over delayed rewards. It
seems to me, this human predisposition like no other lies at the heart
of many mistakes in software development, including failed attempts
adopting Test-Driven Development (TDD).

But first, let's look at the research on Hyperbolic Discounting. The
inclination to favor immediate rewards over long-term rewards is also
observed in animals and is likely to be a remainder of our animalistic
past. Animals, for the most part, do not show the ability to postpone
gratification. One particularly famous example, illustrating our human
struggle to deal with delayed gratification is the [Stanford Marshmallow
experiment][]. In this experiment children were offered a small,
immediate reward (e.G. a single marshmallow) or a bigger, delayed reward
(e.G. two marshmallows in 15 Min). <!--more--> The rational thing to do,
would be to wait a bit. Needless to say it took the kids a lot of effort
to resist immediate gratification:

<iframe width="560" height="315" src="http://www.youtube.com/embed/QX_oy9614HQ" frameborder="0" allowfullscreen></iframe>

What's interesting is that these experiments not only illustrate our
difficulty resisting immediate gratification, but also found that
children with the ability to wait longer for the preferred rewards
tended to have better life outcomes, as measured by SAT scores,
educational attainment, body mass index (BMI) and other life measures.
Every developer reading this will probably remember a case where he/she
tried to solve an issue the simple, elegant way, eventually resorting to
some kind of hack due to unforeseen issues or perceived time pressure.
Being "done" early and especially being "done" on time is gratifying to
us.

How do these observations relate to the adoption of Test-Driven
Development? Test-Driven development has been shown to reduce the amount
of defects in software by researchers at [IBM][] and [Microsoft][]. TDD
has also been shown to point out flawed design- and architectural
aspects of software, as pointed out in the talk "[The Deep Synergy
Between Testability and Good Design][]" by Michael Feathers. In my
experience however, the biggest payoff for the Test-Driven approach is
the ability to rapidly fix mistakes you make later on. The significant
test coverage obtained by test-driving code acts as a safety net -
catching most of the mistakes you will inevitably make along the way,
cleaning and refactoring your code. It is the only professional way I
know, to confidently keep large code basis from rotting. This fact has
been stressed by Uncle Bob over and over and over again.

And yet it seems to me that software developers rarely embrace
Test-Driven Development. Why is that? I suppose it is not only because
of the steep learning curve. My former colleague [Benedikt Eger blogged
about that (in German)][]. From an emotional point of view Test-Driven
Development is a developer's nightmare. It will make you feel bad. It
will challenge you to think about the problem and how to test it, before
even writing the first, gratifying line of ("real", productive) code. It
will point out the flaws in your design and make testing hard every time
you get it wrong. And last but not least, you will feel like you could
be so much faster, if only you wouldn't have to write these stupid
tests. And all that for the delayed gratification of being able to
confidently alter code a few months or years from now.

Needless to say, I think you should resist the temptation of immediate
gratification. Instead, try at least to do the right thing and start
with a test. You might not immediately be able to test-drive 100% of the
code you write, but as time progresses you will improve and find ways to
test these spots you missed earlier. Be aware of the Hyperbolic
Discounting fallacy and practice self-control. Your patience and
discipline will be rewarded tenfold, eventually. It is the rational
thing to do.

  [We're All Predictably Irrational]: http://www.youtube.com/watch?v=JhjUJTw2i1M
  [Hyperbolic Discounting]: http://en.wikipedia.org/wiki/Hyperbolic_discounting
  [Stanford Marshmallow experiment]: http://en.wikipedia.org/wiki/Marshmallow_experiment
  [IBM]: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.129.7992
  [Microsoft]: http://research.microsoft.com/en-us/groups/ese/nagappan_tdd.pdf
  [The Deep Synergy Between Testability and Good Design]: http://vimeo.com/15007792
  [Benedikt Eger blogged about that (in German)]: http://www.zustandsforschung.de/index.php/tdd-ist-ganz-schoen-schwer/
