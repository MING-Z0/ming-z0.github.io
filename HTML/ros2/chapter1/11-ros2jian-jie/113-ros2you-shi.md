### 1.1.3 ROS2优势

#### 1.ROS与其他机器人软件框架比较

ROS是构建机器人的最快捷方式！

##### 1.1 开源

ROS一直是开源的，并且将永远是开源的，以确保全世界的爱好者、开发人员可以自由、不受限制地访问高质量、一流、功能齐全的机器人SDK。另外官方也在其他开源项目之上构建ROS，ROS会尽可能的利用并遵循开放标准（例如OMG的DDS）。

##### 1.2 免费

官方鼓励用户对ROS做出开源贡献，也欢迎提出宝贵意见，但不干涉开发者将ROS集成进非开源软件，不反对将ROS集成进专有产品。

##### 1.3 多平台支持

ROS2支持Linux、Windows和macOS以及各种嵌入式平台（通过micro-ROS）并且不同平台都已经通过了官方测试，这意味着通过ROS2可以实现开发、部署后端管理系统和用户界面的无缝衔接。分层支持模型还允许将ROS2移植到诸如实时和嵌入式操作系统等新平台上，以便在获得关注和投资时将ROS2引入和推广到这些新平台中。

##### 1.4 应用领域广泛

ROS可以在各种机器人应用中使用，从室内到室外，从家用到汽车，从水下到太空，从消费市场到工业领域，ROS都可以独当一面。

##### 1.5 全球化社区

十多年来，ROS项目通过培育由数百万开发人员和用户组成的全球化社区，为机器人技术做出贡献和改进，从而产生了一个庞大的机器人软件生态系统。 ROS由该社区开发并为该社区服务，该社区将成为其未来的管理者。

##### 1.6 可缩短产品上市时间

ROS提供了开发机器人应用程序所需的工具、库和功能，使开发者可以将更多的时间花费在与自身业务相关的工作上。由于它还是开源的，所以开发者可以决定何时何处使用ROS，甚至还可以根据自身需求修改ROS。另外ROS是友好的，不具排他性，开发者可以在ROS和其他机器人软件框架之间自由选择，或者也可以将ROS与其他软件框架集成，以取长补短。

##### 1.7 广泛的行业支持

业界对ROS的支持非常强大。除了在ROS上开发产品外，来自世界各地的大大小小的公司都在投入资源为ROS做出开源贡献。

##### 1.8 业界肯定

整个机器人行业都依赖于ROS。ROS是教授机器人技术的标准，是大多数机器人研究的基础，从单个学生项目到多机构合作再到大型​​竞赛，ROS都占据着主导地位。世界各地不计其数的机器人内部都运行着ROS，仅在自主移动机器人 \(AMR\) 中，ROS就帮助创造了数十亿美元的价值。

#### 2.ROS2较之于ROS1的优势

ROS2是全新一代机器人操作系统，不只是功能增强的ROS1。

##### 2.1 去中心化

在ROS1中使用master节点管理调度ROS系统，这存在极大的安全隐患，一旦master节点异常退出，那么会导致整个系统的崩溃。在ROS2中采用了去中心化，各个节点之间无需通过master关联，各个节点都是等态的，可以相互发现彼此。

##### 2.2 全新通信底层实现

秉着不重复发明轮子的原则，ROS2不再自实现通信底层，而是直接更换为DDS通信，这使得ROS2较之于ROS1无论是通信的实行性、可靠性还是连续性都有大幅度提升。

##### 2.3 应用场景更为广泛

ROS1在设计之初有着天生的硬件优势以及局限性：

* 单机；
* 工作站级的计算资源；
* 无实时性要求（有此类需求也可以以特殊方式满足）；
* 出色的网络连接（有线或近距离高带宽无线）；
* 主要用于学术界；
* 灵活有余而约束不足。

这导致了它的一些先天性缺陷，不能适应新时代的需求，比如：

* 对多机器人编队支持欠佳；
* 小型嵌入式平台不能很好的支持ROS；
* 实时性差；
* ROS之间的数据传输受网络质量影响严重；
* 产品不易落地。

随着ROS2的推出，上述场景的缺陷都得到很大程度的修复。

##### 2.4 大量采用新技术、新的设计理念

随着ROS十数年的发展，大量的新技术也产生、改进、成熟并被广泛采用，ROS也开始引入并应用一些新技术，比如：

* DDS（ Data Distribution Service——数据分发服务）；

* Zeroconf；

* ZeroMQ；

* Redis；

* WebSockets。

这些新技术为ROS带来了更多的便利，比如：更少的维护成本，却有着更多的功能拓展，并且随着第三方库的升级而持续受益。

此外，ROS2还重构了API系统，改进了ROS1的API在设计上的不足。
