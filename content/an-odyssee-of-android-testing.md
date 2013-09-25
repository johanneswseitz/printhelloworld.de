Title: An Odyssee of Android testing
Date: 2012-05-01 23:07
Author: joseitz
Slug: an-odyssee-of-android-testing

A few days ago I started developing my first native Android App. Finally
a green field project! Finally, an opportunity, to do things right!
Finally, a project I could develop in a Test-Driven fashion without the
weight of any legacy cruft slowing me down! Or so I thought...

With a lot of enthusiasm I bootstrapped a new Maven Project and sure
enough there was an Archetype with something called "Instrumentation
Tests" included. At that point I had no idea what an "Instrumentation
Test" might be, but I thought, if it's got the word Test in it, it can't
hurt, right?

![Maven archetypes screenshot](|filename|/images/maven-archetypes.png)

When I checked the pom.xml file, I noticed there was no JUnit dependency
and also the archetype did not generate the usual "src/test" directory
sibling of "src/main". Well, nothing I can't fix. So I threw in my usual
test dependencies and started out writing tests in "src/main", ignoring
the instrumentation project Maven created for now. In retrospect I
should have seen the signs on the wall...

#### Shadowy depencencies

I wrote a first test to check the "title" property of my main activity.
Nothing too fancy. I hit the run key. And sure enough, my JUnit bar
turned red. But wait a minute... What kind of strange test failure is
that?

    !!! JUnit version 3.8 or later expected:

    java.lang.RuntimeException: Stub!  
    at junit.runner.BaseTestRunner.<init>(BaseTestRunner.java:5)  
    at junit.textui.TestRunner.<init>(TestRunner.java:54)  
    at junit.textui.TestRunner.<init>(TestRunner.java:48)  
    at junit.textui.TestRunner.<init>(TestRunner.java:41)  
    ...

![Junit Version failure screenshot](|filename|/images/junit-version-failure.png)

As it turns out, Google includes their own version of JUnit 3 with the
Android SDK. So no JUnit 4 for me! Too bad. Later I figured out you can
work your way around this issue by moving the JUnit 4 dependency before
the Android dependency in your IDEs Classpath configuration. If you are
developing in IntellJ IDEA you can do so in the "Project Structure"
dialog, as shown on the right. And don't forget to move your JUnit
depdency above the Android depdencies in your pom.xml file as well,
otherwise your CI and console build will run into similar trouble.

![IntelliJ Dependency order screenshot](|filename|/images/intellij-dependency-order.png)

#### Vicious Relatives

At first it didn't seem like the dependency order trick worked for me,
until I took a better look and noticed the error message had changed
slightly. No I was faced with a different error. It read:

    java.lang.RuntimeException: Stub!     
      at android.content.Context.(Context.java:4)     
      at android.content.ContextWrapper.(ContextWrapper.java:5)     
      at android.view.ContextThemeWrapper.(ContextThemeWrapper.java:5)     
      at android.app.Activity.(Activity.java:6) ...

After some debugging, decompilation and googling I found that Android
classes my objects need to implement, like the 'android.app.Activity'
class are rigged to throw this exception. WTF? For some reason Google
decided to not to include the "real" implementations of (some?) API
classes in the SDK and replaced them with mere Placeholders. Vicious
placeholders with constructors rigged to throw devious exceptions. These
classes are amongst truly the most vicious, test-averse framework code I
have seen so far.

#### My way or the Google way

At this point I was faced with a choice: give in to Google and try their
official way of testing they call "Instrumentation testing" or start
mocking out the whole Google API enchilada. I decided to try the Google
way of Android testing first. I read through [the awful android testing
documentation][] (Please! Documentation writers: less bla bla, more
working code samples!). At some point I had it figured out. I derived my
Test class from the [ActivityInstrumentationTestCase2][] class, rewired
some methods and hit the run button. Good thing I generated the project
to include the test subproject from the start!

This time the test would not run in my IDE window because apparently the
version of JUnit Google includes with the Android SDK is incompatible
with my IDE. I tried the Maven test target on the IT project but my
console told me that none of the tests ran. I found that I had to run
the Maven "install" lifecycle goal in order for the tests to run. That
doesn't make any sense... but fair enough. Here goes:

![No devices attached error screenshot](|filename|/images/no-devices-attached-error.png)

No devices Attached? Oh right, it's an integration test target. It needs
a device to run. Big bummer.

I attached a test device and the whole process of installing the app on
the device and running the tests finally worked. It took pretty long
though - between 40 sec. and 1 minute. And what's even worse - my
mocking libraries (Mockito, EasyMock) turned out to be incompatible with
the Dalvic VM. And what's worse: I don't want to have an Android Device
plugged into my CI Server all the time just to run my tests... or have
the horribly slow Android Emulator starting and shutting down all the
time. So... while the Google way might be okay for UI- or real
integration testing it is unsuitable to the rapid iteration that is TDD.
I need my tests to be fast as hell. And also, I don't want to work
without a Mocking library.

#### Salvation

So, at this point I was frustrated enough to consider just mocking the
whole Google framework. Every. Single. Class. But hark! There is hope,
yet! After a few hours of googling for alternatives and workaround I
found a promising project on Github called [Robolectric][]. What these
guys managed is nothing short of genius. They simply shadow the Google
API dependencies in your project.

That's it. It's so easy, it's so simple! All of the hostile 'Stub!'
exceptions: gone! Almost too good to be true. And it works! It actually
works! All you really need to do, is add this one Maven dependency to
your project:

    <dependency>
        <groupId>com.pivotallabs</groupId>
        <artifactId>robolectric</artifactId>
        <version>X.X.X</version>
        <scope>test</scope>
    </dependency>    

... configure your JUnit 4 Tests to use the RobolectricTestRunner and
that's it!

![No devices attached error screenshot](|filename|/images/robolectric-man.png)

#### Epilogue

I probably could have hidden most of my code behind a boundary. As a
matter of fact that's what I do for "business logic" - the real
"brainpower" of the app. But there are still valid test cases that
require me to access decedents of the Android SDK classes. For now I am
happy to work with Robolectric, in order to test such cases in a fast
and easy manner on my development machine, with no devices attached or
emulators running.

What shocked me is that Google, a company known for their dedication to
technical excellence would come up with a framework that is so hostile
towards such an important practice as TDD. Coming from iOS and the
pretty testable Cocoa Touch Framework I expected the Android Testing to
be on par with the Java platform (far ahead of the Apple world). Imagine
the shock I felt, when I noticed just how wrong I was. As agile methods
and practices seem to take over the industry, vendors should pay more
attention to properties that are essential to rapid development and
frequent delivery - such as simple and fast automated testing.

  [the awful android testing documentation]: http://developer.android.com/guide/topics/testing/testing_android.html
  [ActivityInstrumentationTestCase2]: http://developer.android.com/reference/android/test/ActivityInstrumentationTestCase2.html
  [Robolectric]: http://pivotal.github.com/robolectric/
