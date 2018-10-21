# beckonjira

Beckon Jira CLI does 2 things

* Generate a branch name
* Open a Jira ticket in the browser

```shell
usage: beckon-jira [-h] [--open] ticket_name

positional arguments:
  ticket_name  Jira Ticket Number (e.g., BASE-12345)

optional arguments:
  -h, --help   show this help message and exit
  --open       Run `open` command instead (default: False)
```


## Install


### PIP

```shell
pip3 install -U git+git://github.com/kkweon/beckonjira.git

```

### Build from source

```shell
python3 setup.py install
```


## Usage

### Create a branch name

```shell
beckon-jira BASE-12345
# same as `beckon-jira 12345`
# or even website `beckon-jira https://beckon.atlassian.net/projects/BASE/issues/BASE-12345`
```

```shell
bug/20181020/BASE-12345-cb3-spider-and-polar-charts-has-label-that-is-obstructed-and-punch-to-edit-showing
```

or one can use `pbcopy` to copy to the clipboard directly

```shell
beckon-jira 12345 | pbcopy
```


### Open in the browser

```shell
beckon-jira 12345 --open # will open the browser with `open` command
```
