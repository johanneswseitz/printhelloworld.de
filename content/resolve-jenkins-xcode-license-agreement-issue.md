Title: Resolving the Jenkins Xcode License Agreement Issue
Date: 2012-04-06 22:36
Author: Johannes Seitz
Category: Continuous Integration iOS
Slug: resolve-jenkins-xcode-license-agreement-issue

When I set up a new Jenkins CI Server on OS X in order to build iOS
Projects I ran into some trouble.

The combination of Xcode 4.3, the Jenkins Xcode Plugin 1.3.1 and the
Jenkins CI Version 1.458 does not seem to play well together. Whenever I
tried to build an Xcode project, the build failed with the following
message:  

` You have not agreed to the Xcode license agreements, please run xcodebuild standalone from within a Terminal window to review and agree to the Xcode license agreements. Build step 'XCode' marked build as failure Finished: FAILURE`  

When I went to the terminal and entered the exact same build command
from the Jenkins logs, the project built just fine. Weird. I googled for
the error message, but did not find anything on the web.  

Soon I discovered the problem: The installer package I got from
http://jenkins-ci.org installed a LaunchDeamon configuration, running
Jenkins as the "daemon" user. This is a good thing for security - but
unfortunately it doesn't work well with the latest Xcode.

The solution is to run the following command:  
` sudo xcodebuild -license`  
This will display the Xcode license agreement, so you can accept it for
all users on your Mac, including the daemon user. Problem solved. Enjoy
your Jenkins Server!
