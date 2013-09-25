Title: Using Git hooks to keep your build stable
Date: 2013-08-13 12:46
Author: Johannes Seitz
Category: Testing
Slug: using-git-hooks-to-keep-your-build-stable

A little known fact is that Git supports client-side hooks to execute a
command line script before certain commands such as `commit` or `push`.
This feature can be used to perform additional quality checks on your
codebase. What's way cool about it is that Git will actually cancel the
action if the [exit status][] code of a script is not zero. This makes
it a perfect fit for automated checks making sure you're not shooting
yourself in the foot.

#### How Git hooks work

Creating a hook is very simple: all you need to do is create a shell
script in the `.git/hooks/` directory of an existing Git repository. You
will find several sample hooks in this directory already. All of these
end with `.sample`, rendering them inactive. If you create your own,
make sure this script file you create starts with a [shebang][] and is
executable.

![Git hooks in the shell](|filename|/images/git-hooks.png)

#### Make hooks test your every commit

I have commit hook perform a full compile and test of my code on every
commit. Not only does this make sure that everything I commit is stable
and working, it also makes cherry-picking commits so much easier and
less risky. Sure it may take some time for the compile and test to run,
but the time you save, hunting down that issue you just inadvertently
pushed to the master branch is closer to zero.

#### Make your TODO comments nag

I dislike the idea of TODO comments. They are usually markers of a
[broken window][] but what's worse is that they tend to invisibly rot
and accumulate. Here's my pre-push hook to keep these broken windows and
untracked tasks in mind:

    #!/usr/bin/env ruby

    def colorize(text, color_code)
      "#{color_code}#{text}\033[0m\n"
    end

    def red(text); colorize(text, "\033[31m"); end
    def green(text); colorize(text, "\033[32m"); end

    def command?(command)
      system("which #{ command} > /dev/null 2>&1")
    end

    def tasks
      puts green('> Checking TODOs...')
      
      todo_files = `find . -not -path "./out/*" -not -path "./play*/*"
                    -name "*.scala" -exec grep -q "TODO" {} \\; -print`

      unless todo_files.empty?
        puts red("> Please fix the following TODOs fist:")
        puts todo_files
        exit 1
      else
        puts green('> All OK')
      end
    end
   
    tasks

#### Share hooks

The way Git hooks work, they are not pushed to the remote repository and
thus not shared with your teammates. A simple solution for this issue is
to keep the hooks in the Git repository themselves and have a script
that symlinks them into the local `.git` directory. You will still need
to execute this script once on every machine, but your git hooks will be
shared, versioned and in-sync.

Here's my symlink script:

    #!/usr/bin/env ruby

    def symlink
      ["pre-commit", "pre-push"].each do |command|
      `ln -s -f ../../git-hooks/#{command} ../.git/hooks/#{command}`
      `chmod +x ../.git/hooks/#{command}`
      end
    end

    symlink

#### Conclusion

In my experience the usage of git hooks for quality assurance to a
certain extend reduces the number of broken builds and broken windows.
It is certainly not a silver bullet, but still worthwhile.

Feel free to add your own ideas and/or suggestions on how to use Git
hooks for quality assurance to the comment section!

  [exit status]: http://en.wikipedia.org/wiki/Exit_status
  [shebang]: http://de.wikipedia.org/wiki/Shebang
  [broken window]: http://en.wikipedia.org/wiki/Broken_windows_theory
