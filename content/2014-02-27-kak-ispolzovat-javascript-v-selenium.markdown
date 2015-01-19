title: "Как использовать javaScript в selenium"
date: 2014-02-27 21:05:32 +0400
categories: javascript, selenium, webdriver, webelement

Иногда в следствии сложной верстки некоторые элементы становятся недоступны/ограниченны для взоимодействия с ними посредством тех методов и свойств, что предоставляет нам интерфейс WebElement. Например есть группа элементов `li` в каком-нить контейнере, часть которых невидима (например имеют стиль `display: none`), и соответственно selenium ругается при попытке например кликнуть по ним. Чтобы кликнуть необходимо проскроллировать этот элемент в видимую облать экрана. Это можно сделать двумя способами:

* с помощью js метода глобального объекта window - `window.scrollTo(x, y)`; где x, y координаты необходиого элемента<!--more-->
* либо с помощью js метода, который есть у каждого элемента DOM - `scrollIntoView()`


        :::java
        public void scrollElementIntoView(WebElement element){
            JavascriptExecutor javascriptExecutor = (JavascriptExecutor) driver;
            javascriptExecutor.executeScript("window.scrollTo("+element.getLocation().x+", 
            "+element.getLocation().y+");");
        }


        public void scrollElementIntoView(WebElement element){
            JavascriptExecutor javascriptExecutor = (JavascriptExecutor) driver;
            javascriptExecutor.executeScript("var element = document.getElementById('"+element.getAttribute("id")+"');" + "element.scrollIntoView();");
        }
