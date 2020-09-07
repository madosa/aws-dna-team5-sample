# AWS SAM - Sample Project

AWS SAM Python 프로젝트의 대략적인 구성을 소개합니다

## 📦 Prerequisites

아래 응용프로그램은 미리 설치가 필요합니다

### 🐳 Docker

`sam build --use-container` 명령이 도커를 필요로 합니다

### 🔐 AWS Credential 설정

`aws configure` 로 원하는 AWS DNA 실습용 IAM Security credentials 를 세팅해야 합니다
미리 `brew instal awscli` 를 설치해두면 좋습니다

## 📂 Project Structure

AWS SAM 의 Python 프로젝트는 다음의 구조가 좋을듯 합니다

\"#" 접두사의 메모가 없는 파일이나 디렉토리는 중요하지 않습니다 

```
 takagi  # 프로젝트 이름
├──  events  # sam local invoke에 사용할 event 파일
│  └──  echo.json
├──  Makefile
├──  poetry.lock
├──  pyproject.toml
├──  README.md
├──  requirements.txt  # sam build에 사용될 프로젝트 의존성 파일
├──  takagi  # main application
│  ├──  decorators.py
│  ├──  functions  # lambda function 코드
│  │  ├──  __init__.py
│  │  └──  echo.py
│  ├──  models.py
│  └──  tests
│     └──  unit
└──  template.yaml  # AWS SAM 정의 파일
```

## 🍰 How to start

파이썬 가상환경을 구성하고, 이 프로젝트에서 사용할 의존성 파일을 설치하면 끝납니다

### Install pyenv

파이썬 가상환경을 설정하기 위한 응용프로그램입니다
Java의 jenv, NodeJS의 nvm과 비슷합니다

```bash
# ✨ NOTE: 아래 단계를 모두 마치면, 이 프로젝트 (takagi) 디렉토리에 위치한경우
# 자동으로 가상환경이 활성화 됩니다

# pyenv 설치
$ curl https://pyenv.run | bash

# 완료되면 아래 내용을 .zshrc (또는 .bash_profile) 에 추가
# NOTE: 명령어를 복사해서 실행하셔도 됩니다
$ cat <<EOF >> ~/.zshrc
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
EOF

# .zshrc (또는 .bash_profile) 갱신
$ source ~/.zshrc

# 지금 프로젝트에서 사용할 Python 3.8.3 버전 설치
$ pyenv install 3.8.3

# 가상환경 생성 (가상환경 이름은 현재 프로젝트 이름인 takagi 로 합니다)
$ pyenv virtualenv 3.8.3 takagi
```

### Install Poetry

`Poetry` 는 파이썬 패키지 매니저입니다.
NodeJS에 기본 패키지 매니저인 `npm` 외에도 `yarn`이 있듯
Python에도 기본 패키지 매니저인 `pip` 외에도 `Poetry`가 있습니다
(편의를 위해 사용합니다)

```bash
# 반드시 이전에 만든 가상환경 (takagi) 이 활성화 된 상태에서 진행하세요
$ pyenv shell takagi
$ pip install poetry
```

### Install Dependencies

지금 프로젝트에서 사용할 의존성 파일을 이전에 설치한 `Poetry`를 써서 설치합니다

```bash
$ poetry install --no-root
```


## Run SAM with AWS-SAM-CLI

다음은 로컬에서 함수를 테스트해보는 방법과 빌드하는법, 배포하는 방법에 대해 설명합니다

### 🚕 Run "SlackEchoFunction" with "sam local invoke"

미리 작성한 Makefile의 명령어를 활용하여 실행할 수 있습니다
소스를 수정하면 새로이 빌드하고, 실행해야 변경된 내용이 반영됩니다

```shell
$ make build
$ make invoke-local-echo
```

### 🚀 Deploy SAM

다음의 명령어로 배포할 수 있습니다

```shell
# 새로 빌드하고, 배포합니다
$ make depoly
```