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

### Available analysis options

| Analysis | Description |
|--------|-------------|
| abs-churn | date,added,deleted,commits |
| age | entity,age-months |
| author-churn | author,added,deleted,commits |
| authors | entity,n-authors,n-revs |
| communication | author,peer,shared,average,strength |
| coupling | entity,coupled,degree,average-revs |
| entity-churn | entity,added,deleted,commits |
| entity-effort | entity,author,author-revs,total-revs |
| entity-ownership | entity,author,added,deleted |
| fragmentation | entity,fractal-value,total-revs |
| identity | author,rev,date,entity,message,loc-added,loc-deleted |
| main-dev | entity,main-dev,added,total-added,ownership |
| main-dev-by-revs | entity,main-dev,added,total-added,ownership |
| messages |  |
| refactoring-main-dev | entity,main-dev,removed,total-removed,ownership |
| revisions | entity,n-revs |
| soc | Sum of coupling |
| summary | statistic,value |

## References

- [Codecharta](https://maibornwolff.github.io/codecharta/)
- [Software Design X-Rays](https://pragprog.com/book/atevol/software-design-x-rays)
- https://www.sonarqube.org/
