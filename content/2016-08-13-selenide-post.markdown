Title: Selenide пост
Date: 2016-08-15 20:25:03
Categories: 

Как-то так получилось, что я обошел вниманием в этом блоге замечательную библиотеку для разработки UI автотестов [Selenide](http://selenide.org/). Сим постом исправляю недоразумение. Данная библиотека по сути обертка над Webdriver, разрабатывается она под флагом компании Codeborne, Андреем Солнцевым. Библиотека open source, под лицензией MIT. Пул реквесты принимаются, если по делу, то без проблем. Так что если есть, что добавить своего, то всегда пожалуйста. Собственно `Selenide` позволяет легко и не принужденно работать с локаторами, элементами, ожиданиями и т.д. При этом позволяет работать с базовым webdriver, если вам по какой-то причине вдруг не хватает этого. 

Если вы никогда не писали тесты используя `Selenium/Webdriver`, я настоятельно рекомендую начать пользоваться ими посредством `Selenide`.
Если вы уберзакостенелый пользователь `Selenium/Webdriver` и еще не используете `Selenide`, я еще более рекомендую начать им пользоваться. 
Первым это позволит начать писать тесты не отвлекаясь на реализацию своих велосипедов(ожидания, проверки и т.д.) и сэкономит кучу времени и нервов, вторым же это позволит наконец-то писать лаконичные, стабильные тесты и по делу.

Итак чем же `Selenide` так прекрасен? Давайте по порядку.

##Ожидания
Сколько копий сломано об решении этой проблемы! Я сам написал с десяток, наверно, раз различные обертки которые реализуют ожидание чего-то и как-то. Теперь это есть в Selenide из коробки, и не нужно задумываться об этом.

```java
//Webdriver
FluentWait<By> fluentWait = new FluentWait<By>(By.tagName("TEXTAREA"));
fluentWait.pollingEvery(100, TimeUnit.MILLISECONDS);
fluentWait.withTimeout(1000, TimeUnit.MILLISECONDS);
fluentWait.until(new Predicate<By>() {
    public boolean apply(By by) {
        try {
            return browser.findElement(by).isDisplayed();
        } catch (NoSuchElementException ex) {
            return false;
        }
    }
});
assertEquals("John", browser.findElement(By.tagName("TEXTAREA")).getAttribute("value"));


//Selenide
$("TEXTAREA").shouldHave(value("John"));

```
##Удобные методы работы с элементами. 
Вы только сравните:

доступ к элементам:
```java
// getting element Webdriver
driver.findElement(By.id("customerContainer"));

// getting element Selenide
$("#customerContainer");

```
проверка на наличие текста:

```java
//Webdriver
assertEquals("Customer", driver.findElement(By.id("customerContainer")).getText());

//Selenide
$("#customerContainer").shouldHave(text("Customer"));

```

##Скриншоты 
которые снимаются как падает тест или в нужном вам месте:
```java
takeScreenShot("my-test-case");
```
##Conditions 
хрен знает как перевести правильно (условия?), но штука очень удобная, посмотрите:
```java 

$(“input”).shouldBe(visible);
$(“input”).shouldBe(readonly);
$(“input”).shouldHave(name(“fname”));
$(“input”).shouldHave(value(“John”))
$(“#input”).shouldHave(type(“checkbox”))

//and more
options
cssClass(String)
focused
enabled
disabled
selected
matchText(String regex)
text(String substring)
exactText(String wholeText)
textCaseSensitive(String substring)
exactTextCaseSensitive(String wholeText)

```

Если вы вдруг пользуетесь `C#`, то есть пока неполный, но вполне работоспособный порт `Selenide` на C#. Найти его можно [тут](https://github.com/yashaka/NSelene). Разрабатывает его Яков Крамаренко.

Кстати, если вы еще не в курсе, то у нас есть прекрасный чатик тестировщиков в слаке, о котором я [рассказывал](/blog/2015/12/18/izvinitelnyi/) недавно. В этом чате есть канал посвященный `Selenide` в котором обитают и сами разработчики как `Selenide` так и `NSelene`. Помимо этого та есть еще куча интересных каналов и людей. Welcome!