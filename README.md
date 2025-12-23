# uv_testpkg

uvを使ってROS 2パッケージを作成するテスト用パッケージ

## このリポジトリの目的

### PEP 668への対応

PEP 668により，Ubunru 24.04（Python 3.12がデフォルト）ではpipによるパッケージインストールには仮想環境の利用が求められる．  
ここで問題になるのが，rosdepコマンドによるROS 2パッケージの依存関係のインストールである．  
rosdepコマンドではaptもしくはpipを使って依存関係をインストールするが，pipによるインストールではシステムのPython環境に直接インストールしようとする．  
しかしながら，先述のPEP 668の制約により，システムのPython環境に直接インストールしようとするとエラーが発生する．  
つまり，**「Pythonを利用するROSパッケージを作成する際に，仮想環境を利用するにはどうすればいいのか？」** というのが本リポジトリの問であり，本レポジトリではuvを利用してこの問題を解決する方法を示す．

### setup.pyからの脱却

ROS 2パッケージのビルドにはcolconを利用，特にPythonで書かれたパッケージにはament_pythonを使用するのが一般的である．  
ament_pythonではsetup.pyを利用するが，最近のPythonコミュニティではpyproject.tomlを活用する流れになっている．  
そのため，**setup.pyを使わずにpyproject.tomlのみでROS 2パッケージを作成する方法** を本レポジトリで検証する．

## 本リポジトリの使い方

### 検証環境

- Ubuntu 24.04
- Python 3.12
- ROS 2 Jazzy
- uv 0.9.18

### 作成したノード

ROS 2 docsのチュートリアルで紹介されているtalkerノードとlistenerノードを利用  
（https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html）

### パッケージのビルドと実行

1. ROS 2のワークスペースを作成，その下にsrcディレクトリを作成して本リポジトリをクローンする．

## 実行結果

### 仮想環境下

```bash
[INFO] [1766487529.482756495] [uv_pip_test_node]: Publishing: "moviepy version: 2.1.2, numpy version: 2.4.0, count: 0"
[INFO] [1766487530.459914040] [uv_pip_test_node]: Publishing: "moviepy version: 2.1.2, numpy version: 2.4.0, count: 1"
[INFO] [1766487531.459868972] [uv_pip_test_node]: Publishing: "moviepy version: 2.1.2, numpy version: 2.4.0, count: 2"
```

### システム環境下

```bash
[INFO] [1766486856.265054331] [uv_pip_test_node]: Publishing: "numpy version: 1.26.4, count: 0"
[INFO] [1766486857.250076879] [uv_pip_test_node]: Publishing: "numpy version: 1.26.4, count: 1"
[INFO] [1766486858.250171210] [uv_pip_test_node]: Publishing: "numpy version: 1.26.4, count: 2"
```
