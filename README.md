# EDA
## 数据源
https://physionet.org/content/picsdb/1.0.0/

## 测试

测试

## 一些参考链接 
EDA Example https://colab.research.google.com/drive/19b9IhncD3AVdCVVZ3oGHs80ZcgTj0d-w?usp=sharing

wfdb Demo

https://github.com/MIT-LCP/wfdb-python/blob/main/demo.ipynb


## 20230124 （这部分的更新在ECG.ipynb，EDA主线在EDA.ipynb）

（1） 关于annotations这部分，提供的文件里应该是没有annotation的，我拆解的多个infant数据里annotation都是空，也无法正常标记；另外第七组这个不是annotation是峰值

(这个是标记)

![](assets/images/1.png)

（2）不过峰值对我们也有用，我们可以自己加标记，因为标记正常和不正常也是心率范围定的，转换心率的方法我记得有了，到时候能根据这些判断一下打标签，生成excel，后面就好说了，就能对的上DR之前课堂上给的EDA流程了


(3) TODO：根据ECG的peak的合理范围判断来打上annotation并据此给正常?非正常的婴儿分类（EDA有些图表很复杂，因此给截取的数据都实际情况判断来annotation也是需要的）


> 目前的发现，ecg转换BPM很复杂，目前我们要做的也是resp和ecg的关系，不建议用bpm范围校准

> 建议研究ecg自身的频率分布来，ecg的y 轴（垂直）表示 ECG 波形的振幅，以毫伏为单位测量。 一个大方块代表 0.5 mV，一个小方块代表 0.1 mV。 