title: "Про атрибуты (Boolean)"
date: 2014-05-31 08:31:39 +0400
categories: webdriver, selenium, html

Как выяснилось атрибуты элементов в HTML бывают разные. Более того, они бывают разных типов. Начнем с **Boolean**:
<!--more-->


Boolean
-------

Есть атрибуты которые имеют значение **boolean** например в HTML 4.01 их не мало:


* `checked`             (input type=checkbox/radio)
* `selected`           (option)
* `disabled`          (input, textarea, button, select, option, optgroup)
* `readonly`         (input type=text/password, textarea)
* `multiple`        (select)
* `ismap`    `isMap`     (img, input type=image)

* `defer`               (script)
* `declare`             (object; never used)
* `noresize` `noResize`  (frame)
* `nowrap`   `noWrap`    (td, th; deprecated)
* `noshade`  `noShade`   (hr; deprecated)
* `compact`             (ul, ol, dl, menu, dir; deprecated)

у булевских атрибутов есть интересное свойство. Само их наличие является `true`. И не важно какое при этом у них значение. Даже если атрибут `selected='false'` то это все равно будет равнозначно `selected='true'`, поэтому selenium всегда возвращает `true` при проверке их значений в исходниках.