# How to contribute

Thank you for reading our contribution guidelines, we are exited to welcome you as a contributer to our project!

Before you start contributing a change/fix or even new code please check the [current list of issues](https://github.com/wvankuipers/gadget-backend/issues) and [open pull requests](https://github.com/wvankuipers/gadget-backend/pulls) in this repo.

## Testing

This project uses [Pytest](https://docs.pytest.org/en/stable/) to run our our tests located in the [tests](tests/) directory.
If you update existing code or add new code please make sure the tests do not fail.

Once you submit a pull request the CI will automatically run the tests and check if the overal coverage is not affected by the changes. If this is the case please correct the issues so we can review and merge your pull request.


## Submitting changes

Please send a GitHub Pull Request to our project with a clear list of what you've done (read more about pull requests). We can always use more test coverage. Please follow our coding conventions (below) and make sure all of your commits are atomic (one feature per commit). And make sure the build automation's all succeed.

Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:

```
$ git commit -m "A brief summary of the commit
>
> A paragraph describing what changed and its impact."
```

Do not forget to add the data migrations when making a database change!

## Conding conventions

Start reading our code and you'll get the hang of it. We optimize for readability:

- We tend to follow the [Flask](https://flask.palletsprojects.com/en/1.1.x/) best practices.
- Configure your editor to use the settings as described in our [EditorConfig](https://EditorConfig.org) file. ([]())
- We use [PyCodeStyle](https://pycodestyle.pycqa.org/en/latest/) to enforce the [PEP-8](https://www.python.org/dev/peps/pep-0008/) codestyle rules.
