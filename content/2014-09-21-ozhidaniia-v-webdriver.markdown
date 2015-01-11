title: "Ожидания в WebDriver"
date: 2014-09-21 13:49:08 +0400
comments: true
categories: webdriver, selenium 
---

Механизм ожидания страниц в WebDriver реализован следующим образом. WebDriver работает с DOM, поэтому он ждет пока `document.readyState == complete`, это поведение справедливо для следующих действий:

* `driver.get()`
* `driver.navigate.refresh()`
* переход на другие страницы посредством взаимодействия с различными элементами страницы

существует опция `pageLoadTimeout` которая позволяет прекратить ожидание и остановить загрузку страницы, имейте в виду в случае если DOM к этому моменту не прогрузится вы получите _TimeoutException_
<!--more-->


```java
driver.manage().timeouts().pageLoadTimeout(60, TimeUnit.SECONDS);
```

помимо этого существуют следующие виды ожиданий: 

###Неявные (Implicit) ожидания
Это глобальные ожидания задаются один раз на всю сессию, смысл этого заключается в том что `driver.findElement()` будет выполнятся до тех пор пока элемент не будет найден, либо пока не пройдет отведенное время ожидание. Задается следующим образом:

```java
driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
```


###Явные (Explicit) ожидания
Когда необходимо подождать что-либо определенное, на помощь приходят явные ожидания. Которые могут реализоваться несколькими способами. Объектом `WebDriverWait` 
```java
 final Wait<WebDriver> wait = new WebDriverWait(driver, 5, 1000);
```
где второй параметр время ожидания в секундах, а третий время в милисекундах которое нужно ожидать перед очередным вызовом проверки наличия элемента(по дефолту 500). Если необходимо вывести сообщение в случае неуспешного завершения ожидания, то код может быть следующим:

```java
 final Wait<WebDriver> wait = new WebDriverWait(driver, 5).withMessage("Element was not found");
```
Во время процесса поиска WebDriver регулярно опрашивает браузер на наличие элемента в DOM модели. При этом существует ряд исключительных ситуаций:

* Если элемент доступен в DOM на момент поиска, но спустя время, в момент его вызова, DOM может измениться. Тогда мы получим StaleElementReferenceException.
* Если элемент отсутствует в DOM на момент вызова – получим `NoSuchElementException`.
* Если элемент был найдем в DOM, но не видим на странице – получим `ElementNotVisibleException`.
* Если элемент изменил координаты – получим `MoveTargetOutOfBoundsException`.

когда подобное случается и нам необходимо эту ситуацию избежать, нужно передать в метод ignoring эти классы исключительных ситуаций:

```java
 final Wait<WebDriver> wait = new WebDriverWait(driver, 5).ignoring(StaleElementReferenceException.class, ElementNotVisibleException.class);
```

Объект `Wait` сам по себе ничего не ждет, есму необходимо сообщить нужное состояние которое он ожидает, посредством его метода `until`. Состояния (conditions) могут быть следующими:

* `visibilityOfElementLocated(By locator)`
* `visibilityOf(WebElement element)`
* `textToBePresentInElement(By locator, String text)`
* `titleContains(String title)`
* `presenceOfElementLocated(By locator)`
* `presenceOfAllElementsLocatedBy(By locator)`
* `invisibilityOfElementLocated(By locator)`
* `invisibilityOfElementWithText(By locator, String text)`
* `elementToBeClickable(By locator)`
* `stalenessOf(WebElement element)`
* `alertIsPresent()`

```java
wait.until(ExpectedConditions.presenceOfElementLocated(By.id("smth")));
```


негативные состояния задаются следующим образом:

```java
wait.until(ExpectedConditions.not(ExpectedConditions.presenceOfElementLocated(By.id("smth")));
```


Есть возможность создавать свои состояния:

```java
 Function <? super WebDriver, Object> isTextPresent = new ExpectedCondition<Object>() {
  @Override
  public Boolean apply(WebDriver webDriver) {
    return  webDriver.findElement(By.tagName("div")).getText().contains("Hello");
  }
 };
```

так же можно воспользоваться классом Predicate
```java
Predicate<WebDriver> isTableLoaded = new Predicate<WebDriver>() {
  @Override
  public boolean apply(WebDriver webDriver) {
    List<WebElement> rows = webDriver.findElement(By.id("table")).findElements(By.tagName("tr"));
    return rows.size() > 1;
  }
};
```


