# Code Analysis Utilities

## Metrics
- https://www.sonarsource.com/resources/white-papers/cognitive-complexity.html
- https://github.com/aim42/aim42/issues/236

## Code Maat

https://github.com/adamtornhill/code-maat

### Setup MacOS

```
brew install leiningen

git clone git@github.com:adamtornhill/code-maat.git
cd code-maat
lein uberjar
cp target/code-maat-1.1-SNAPSHOT-standalone.jar ~/bin/code-maat.jar
```

### Usage

Hello World:
```
cd $REPO
git log --all --numstat --date=short --pretty=format:'--%h--%ad--%aN' --no-renames > /tmp/gitlog.txt
java -jar ~/bin/code-maat.jar --log /tmp/gitlog.txt --version-control git2
```

Show help:
```
java -jar ~/bin/code-maat.jar --help
```

Find the main developer of files:
```
java -jar ~/bin/code-maat.jar --log /tmp/gitlog.txt -c git2 -a refactoring-main-dev | grep $DEVELOPER_NAME
```



## References

- [Codecharta](https://maibornwolff.github.io/codecharta/)
- [Software Design X-Rays](https://pragprog.com/book/atevol/software-design-x-rays)
- https://www.sonarqube.org/
