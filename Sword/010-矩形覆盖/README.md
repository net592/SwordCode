问题：
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
比如n=3时，2*3的矩形块有3种覆盖方法：
描述：
这是一道规律题。
知识点：递归，记忆递归，动态规划，递推
难度:：一星
题解：
矩阵覆盖问题
问题分析：
对于很多递归问题，我们都可以通过归纳总结来找出他们的规律：
当n=1时，way=1(横或竖)
当n=2时，way=2(全横或全竖)
当n=3时，way=3(全竖&横横竖&竖横横)
当n=4时，way=5(全竖&全横&竖横横竖&竖竖横横&横横竖竖)
当n=5时，way=8(全竖&竖横横竖竖&竖横横横横&竖竖横横竖&竖竖竖横横&横横竖竖竖&横横横横竖&横横竖横横)
.......
n=(n-1)+(n-2);
于是问题有转换成了之前的斐波那契数列问题了，依旧时同样的方法求解：