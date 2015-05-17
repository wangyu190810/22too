###rust linux 初体验

就在昨天rust发布了1.0版本，开始了自己正式的linux rust 之旅

四月多回学校之后，开始在闲暇时间接触rust，当初想要学习rust的原因，个人觉得自己缺一门语言，即使现
在的python写的还成（自己的代码很垃圾，感觉有点不要脸了）

1. python的性能问题，这个都是大家老生常谈的事情，经常在写脚本时，处理一些数据，但是python运行时
间有时达到了半个小时以上，尽管有各方面的问题，但是自己也是明确的感觉到了python的性能问题，而不是从
他人那里知道的，自己实践过才能知道，自己为什么要做什么

2. python跨平台问题，尽管你可以说python是完备的语言，跨平台问题就不是问题，但是当你要写一个桌面
应用程序时，你就要开始选择是使用pyqt，还是pytk ，即使选好了，开始写也是感觉不太完美（好吧其实这个不算理由）

3. 技术在不断的发展，2010年安卓还是刚刚起步的样子，现在已经发展到了这样的地步，不得不说，如果一门
新的技术出现时，我们没有去学习，自己可能就会脱离这个快速发展的行业，rust的出现，让我不用再回去学习c++了，
可能真是个人愚钝，不能很好的学习好c++，rust的出现，让我有了一个更好的选择机会

####个人实践


从[rust-lang](http://www.rust-lang.org)下载对应版本,之前在win7 64 位下写程序，但是有个gcc
依赖问题，耗费了好久也没有解决，于是最终放弃了win7 64平台，在虚拟机上跑rust

全文例子在linux ubuntu 14.04下通过

1. 安装
    
    rust的源码编译安装是官方给出的方案，本人能力有限，所以源码安装到了最后失败了，最后使用二进制包安装
    
    下载下来之后解压一下，其中有个install.sh 这个是安装脚本
    
        sudo bash install.sh
    
    等待一下，就能安装成功了
    
    还有一种安装方式
    
        sudo  curl -sSf https://static.rust-lang.org/rustup.sh | sh
     
    下来开始检测linux是否安装成功

        xxxx@ubuntu:~$ rustc -V
        rustc 1.0.0 (a59de37e9 2015-05-13) (built 2015-05-14)

    成功安装完成
        
    rust的包管理器使用了cargo这个软件，在我们安装rust的时候，cargo已经安装了

2. hello world
    
    
    我们开始写第一个rust程序
    
        mkdir -p code/rust
        cd code/rust
        
    创建一个first.rs 文件，
    
        fn main(){
            println！("hello {}","world")
        }
   
    保存退出执行:
    
        rustc first.rs
        
    如果没有错误会编译完成，产生一个first的可执行文件，如果在win下产生一个first.exe
    
         ./first
         hello world
         
    伟大的hello world 完成了
        
    想要写更多的东西，就去看看[rustbyexample](http://rustbyexample.com/)
    
3. cargo的使用
    
    在python中我们要使用一个非标准库的包时，比如requests，就要使用pip来安装这个包
    
    在rust中，同样我们也会有这样的需求的
    
    cargo这个是一个极佳的包管理器
    
        cargo new site-demo
        
    这个时候我们能看到产生了site—demo的文件夹
    
        .
        ├── Cargo.toml
        └── src
        └── lib.rs

        1 directory, 2 files

    当前有这些文件，在src的文件夹下创建一个main.rs文件，文件夹目录
        
        .
        ├── Cargo.toml
        └── src
        ├── lib.rs
        └── main.rs

        1 directory, 3 files
    
    然后编译:
        
        cargo build
        
    再次看目录结构：
    
         .
        ├── Cargo.lock
        ├── Cargo.toml
        ├── src
        │   ├── lib.rs
        │   └── main.rs
        └── target
            └── debug
                ├── build
                ├── deps
                ├── examples
                ├── libsite_demo.rlib
                ├── native
                └── site-demo
        
        7 directories, 6 files

    出现了一个site-demo的可执行文件（在win下是site-demo.exe）
    
    执行项目:
    
        cargo run
        
            Running `target/debug/site-demo`
        hello world
   
    这可以就算是一个一个项目的雏形了
    
    当一个项目稳定时，或者一些功能开发完时，我们就要发布最终的版本了,运行：
        
        cargo build --release
        
    再看目录结构：
    
         .
        ├── Cargo.lock
        ├── Cargo.toml
        ├── src
        │   ├── lib.rs
        │   └── main.rs
        └── target
            ├── debug
            │   ├── build
            │   ├── deps
            │   ├── examples
            │   ├── libsite_demo.rlib
            │   ├── native
            │   └── site-demo
            └── release
                ├── build
                ├── deps
                ├── examples
                ├── libsite_demo.rlib
                ├── native
                └── site-demo
        
        12 directories, 8 files

    文件有点多，这个就是cargo的基本使用
    
4.  使用cargo来管理第三反包：

    个人是做web后端开发的，所以就用了rust的web框架,来看看rust的web框架
    
    1. [iron](http://ironframework.io/)
    2. [nickel](http://nickel.rs/)
    
    都可以试试
    
    使用iron创建一个hello world（好吧，貌似只会写这些）
    
    我们在刚刚创建的项目中继续开始,打开Cargo.toml:
    
        [package]
        name = "site-demo"
        version = "0.1.0"
        authors = ["22too"]

    看到了刚刚的信息，版本号和作者，我们在其中添加一下信息:
    
        [dependencies.iron]
        version = "*"
    
    最终变为：
            
        [package]
        name = "site-demo"
        version = "0.1.0"
        authors = ["xxx"]
        
        
        [dependencies.iron]
        version = "*"
    
    这个时候，表示我们把依赖的包iron添加到了项目中，但是这个iron又会依赖其他的项目？在iron的
    cargo.toml中添加了依赖，所以我们仅仅添加当前依赖就行了
    
    编译一下：
    
        cargo build
        
    报错了:
    
         Updating registry `https://github.com/rust-lang/crates.io-index`
         Downloading groupable v0.2.0
         Downloading regex v0.1.30
         Downloading mustache v0.6.1
         Downloading hyper v0.3.16
         Downloading nickel v0.4.0
           Compiling regex v0.1.30
           Compiling groupable v0.2.0
           Compiling mustache v0.6.1
           Compiling openssl-sys v0.6.2
        Build failed, waiting for other jobs to finish...
        failed to run custom build command for `openssl-sys v0.6.2`
        Process didn't exit successfully: `/home/xxx/workspace/site/target/debug/build/openssl-sys-5040130ff99796a0/build-script-build` (exit code: 101)
        --- stdout
        .
        .
        .
        running: "cc" "-O0" "-c" "-ffunction-sections" "-fdata-sections" "-m64" "-fPIC" "/home/xxx/.cargo/registry/src/github.com-1ecc6299db9ec823/openssl-sys-0.6.2/src/old_openssl_shim.c" "-o" "/home//workspace/site/target/debug/build/openssl-sys-5040130ff99796a0/out/src/old_openssl_shim.o"

        
        command did not execute successfully, got: exit code: 1
        
        
        
        --- stderr
        /home/xxx/.cargo/registry/src/github.com-1ecc6299db9ec823/openssl-sys-0.6.2/src/old_openssl_shim.c:1:26: fatal error: openssl/hmac.h: No such file or directory
         #include <openssl/hmac.h>
                                  ^
        compilation terminated.
        thread '<main>' panicked at 'explicit panic', /home/xxx/.cargo/registry/src/github.com-1ecc6299db9ec823/gcc-0.3.5/src/lib.rs:384
        
    在openssl开发库这里报错了,查了一下，是说没有这个库，于是安装：
        
        sudo apt-get install libssl-dev

    继续执行：
        
        wangyu@ubuntu:~/workspace/code/rust/site-demo$ cargo build 
        Updating registry `https://github.com/rust-lang/crates.io-index`
        Compiling lazy_static v0.1.10
        Compiling pkg-config v0.3.4
        Compiling gcc v0.3.5
        Compiling traitobject v0.0.1
        Compiling matches v0.1.2
        Compiling unicase v0.1.0
        Compiling typeable v0.1.1
        Compiling traitobject v0.0.3
        Compiling modifier v0.1.0
        Compiling bitflags v0.1.1
        Compiling rustc-serialize v0.3.14
        Compiling libc v0.1.7
        Compiling httparse v0.1.2
        Compiling error v0.1.7
        Compiling unsafe-any v0.4.1
        Compiling time v0.1.25
        Compiling openssl-sys v0.6.2
        Compiling typemap v0.3.2
        Compiling log v0.3.1
        Compiling num_cpus v0.2.5
        Compiling plugin v0.2.6
        Compiling mime v0.0.11
        Compiling openssl v0.6.2
        Compiling url v0.2.34
        Compiling conduit-mime-types v0.7.3
        Compiling cookie v0.1.20
        Compiling hyper v0.5.0
        Compiling iron v0.1.17
        Compiling site-demo v0.1.0 (file:///home/wangyu/workspace/code/rust/site-demo)

    完成依赖库的安装，下来开始写web版的hello world，打开src/main.rs文件，将这个[例子写入](http://ironframework.io/)
        
        extern crate iron;
        
        use iron::prelude::*;
        use iron::status;
        
        fn main() {
            fn hello_world(_: &mut Request) -> IronResult<Response> {
                Ok(Response::with((status::Ok, "Hello World!")))
            }
        
            Iron::new(hello_world).http("localhost:3000").unwrap();
            println!("On 3000");
        }

    编译一下:
    
        cargo build
        
    编译完成:
    
        .
        ├── Cargo.lock
        ├── Cargo.toml
        ├── src
        │   ├── lib.rs
        │   └── main.rs
        └── target
            ├── debug
            │   ├── build
            │   │   ├── openssl-sys-5040130ff99796a0
            │   │   │   ├── build-script-build
            │   │   │   ├── out
            │   │   │   │   ├── libold_openssl_shim.a
            │   │   │   │   └── src
            │   │   │   │       └── old_openssl_shim.o
            │   │   │   └── output
            │   │   └── time-e758cbe877e9589d
            │   │       ├── build-script-build
            │   │       ├── out
            │   │       │   ├── libtime_helpers.a
            │   │       │   └── src
            │   │       │       └── time_helpers.o
            │   │       └── output
            │   ├── deps
            │   │   ├── libbitflags-518ea12e21428edd.rlib
            │   │   ├── libconduit_mime_types-1e81c78d29a43be5.rlib
            │   │   ├── libcookie-06b0342919872728.rlib
            │   │   ├── liberror-d564459ef07110c0.rlib
            │   │   ├── libgcc-982b24959a427c6e.rlib
            │   │   ├── libhttparse-262bba09b9a8af87.rlib
            │   │   ├── libhyper-7af3be4b39937ea7.rlib
            │   │   ├── libiron-87b54b416aeb130f.rlib
            │   │   ├── liblazy_static-953c0e8789f76850.rlib
            │   │   ├── liblibc-674726c388d62fa2.rlib
            │   │   ├── liblog-54cf393d3c69686f.rlib
            │   │   ├── libmatches-68db25b520030534.rlib
            │   │   ├── libmime-e3d384f950d18291.rlib
            │   │   ├── libmodifier-43745f03a85dbd92.rlib
            │   │   ├── libnum_cpus-51b2c6c8fecf9ef6.rlib
            │   │   ├── libopenssl-a36d86f1beea2185.rlib
            │   │   ├── libopenssl_sys-5040130ff99796a0.rlib
            │   │   ├── libpkg_config-915289378d7b38e9.rlib
            │   │   ├── libplugin-3a7a2e6890e6fef2.rlib
            │   │   ├── librustc_serialize-9ef26f158d5284e0.rlib
            │   │   ├── libtime-e758cbe877e9589d.rlib
            │   │   ├── libtraitobject-5421cd207a7a63b6.rlib
            │   │   ├── libtraitobject-dc1e70e5c4501fdd.rlib
            │   │   ├── libtypeable-e1c7f5ec8654ad3e.rlib
            │   │   ├── libtypemap-3869793a80fd19d6.rlib
            │   │   ├── libunicase-29c711cff0d04b16.rlib
            │   │   ├── libunsafe_any-a082092056257a0f.rlib
            │   │   └── liburl-beb2c5952735425a.rlib
            │   ├── examples
            │   ├── libsite_demo.rlib
            │   ├── native
            │   └── site-demo
            └── release
                ├── build
                ├── deps
                ├── examples
                ├── libsite_demo.rlib
                ├── native
                └── site-demo
        
        18 directories, 44 files
           
    看到了无数的文件，当前release中的可执行文件依旧是刚刚我们执行的hello的可执行文件，不是这次生成的,为了消除歧义，在执行一次编译：
    
        cargo build --release
        Compiling unicase v0.1.0
        Compiling modifier v0.1.0
        Compiling httparse v0.1.2
        Compiling gcc v0.3.5
        Compiling typeable v0.1.1
        Compiling rustc-serialize v0.3.14
        Compiling pkg-config v0.3.4
        Compiling lazy_static v0.1.10
        Compiling bitflags v0.1.1
        Compiling traitobject v0.0.3
        Compiling libc v0.1.7
        Compiling matches v0.1.2
        Compiling traitobject v0.0.1
        Compiling error v0.1.7
        Compiling unsafe-any v0.4.1
        Compiling num_cpus v0.2.5
        Compiling log v0.3.1
        Compiling time v0.1.25
        Compiling openssl-sys v0.6.2
        Compiling typemap v0.3.2
        Compiling mime v0.0.11
        Compiling plugin v0.2.6
        Compiling openssl v0.6.2
        Compiling url v0.2.34
        Compiling conduit-mime-types v0.7.3
        Compiling cookie v0.1.20
        Compiling hyper v0.5.0
        Compiling iron v0.1.17
        Compiling site-demo v0.1.0 (file:///home/wangyu/workspace/code/rust/site-demo)

    完成编译,现在的release已经是web的了
    
    运行：
        
        cargo run
          
          Running `target/debug/site-demo`
    
    [在浏览器查看](http://127.0.0.1:3000):
        
        hello world
     
    基本结束
        
    
    
    
    
        
    
    
    
        
                    
                    
            
            
