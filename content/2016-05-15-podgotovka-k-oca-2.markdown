Title: Подготовка к OCA chapter 2
Date: 2016-05-15 15:25:03
Categories: 

Продолжается подготовка к OCA. На этой неделе грыз главу вторую книги [OCA: Oracle Certified Associate Java SE 8 Programmer I Study Guide: Exam 1Z0-808](http://www.amazon.ca/OCA-Certified-Associate-Programmer-1Z0-808-ebook/dp/B00R04DF3I?ie=UTF8&qid=1462240625&ref_=tmm_kin_swatch_0&sr=8-1) под названием: Operators and Statements.

На очереди следующий набор странностей, о которых нужно знать  и поскорее забыть после экзамена :) 

если вы думаете, что следующее выражение некорректно, то вы ошибаетесь:
```java
int x = 5;
System.out.println(x > 2 ? x < 4 ? 10 : 8 : 7);
```
насчет следующего скорее всего тоже:
```java
if (false) System.out.println("f");
else System.out.println("Failure");
```
слышали что-нибудь про Numeric promotion? Нет? Тогда профуканый вопрос на экзамене станет для вас сюрпризом, и получите неизбежную ошибку компилятора в следующем случае:
```java
byte x = 5;
byte y = 15;
byte z = x + y;
```
следующий пример тоже относится к Numeric promotion, он не скомпилируется:
```java
long x = 10;
int y = 5;
y = y * x;
```
а вот так скомпилируется:
```java
long x = 10;
int y = 5;
y *= x;
```
Удивлены? Я тоже. 
Еще в Java можно так:
```java
boolean b = false;
if (b=true){
...
}
```

Едем дальше. На очереди Core Java API.


