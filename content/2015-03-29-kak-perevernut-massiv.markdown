title: "Вопросы на интервью. Как перевернуть массив? "
date: 2015-03-29 9:38:04 +0400

Один из популярнейших вопросов на интервью для java-девелопера  это просьба перевернуть массив. Это очень похоже на вопрос из прошлой статьи, про переворачивание [строки](/blog/2014/07/07/voprosy-po-java-na-interviu-2/), но немного про другое.  Вопрос не выглядит сложным, все что нужно сделать это создать новый массив такого же размера, перебрать исходный массив от конца до нажала заполняя новый. Все, готово. Но нет, мы же создали дополнительный массив того же размера, что и исходный, что усложняет наше решение `O(n).` Мы не сможем использовать наше решение, если размер массива очень большой (например 10 млн элементов), а размер heap небольшой. Что мы можем тут сделать? Как улучшить наше решение? Можем ли мы перевернуть массив не создавая дополнительный буффер? Для нашей задачи предположим, что у нас массив из `integer` (вообще на интервью хорошая практика задавать правильные вопросы в правильных местах, как говорят знающие люди это черта хорошего программиста). Ключевое тут понять, что вам нужно перевернуть исходный массив, мы не можем использовать другой массив, но использовать одну две дополнительные переменные, вполне допустимо. Так же недопустимо использование сторонних библиотек или `Java API ` которые могут сделать эту работу за нас, а также методов класса `java.util.Arrays`, за исключением `Arrays.toString()` чтобы выводить массивы. Когда наши требования выяснены приступим к решению задачи. 

Первое что приходит в голову это перебрать все элементы массива и поменять их местами. Первый элемент и последний, второй элемент с предпоследним, и т.д. В этом случае все элементы массивы будут перевернуты без использования дополнительного буффера. Ключевая вещь здесь, которую нужно держать в голове это только что нам нужно менять местами элементы до того момента как мы достигнем середины массива, иначе мы получим тот же самый массив. Возникает закономерный вопрос, а что если массив имеет четное количество элементов? В этом случае в середине массива будут два элемента, и нам нужно поменять их местами, поэтому наше условие перебора будет содержать выражение `index <= middle` а не `index < middle`. Середина тут ничто иное как `length/2`. Помните что мы будем использовать     оператор `/` что означает в случае если `length` равно 8, вернет нам 4, а в случае если `length` равно 7, вернет нам 3. Так что в случае четного количества элементов средние элементы поменяются местами, а в случае нечетного средний элемент останется на месте. 


Как говорится, лучше один раз увидеть, чем 100 раз прочитать.
![Array]({filename}/images/gallery/other/Reverse_Array_in_Place_in_Java.png)

Ниже пример моей программы, которая переворачивает массив в один проход, так же неплохо будет посмотреть на юнит тесты к этому коду далее для лучшего понимания.

    :::java
    import java.util.Arrays;

    /**
     * Java Program to demonstrate how to reverse an array in place.
     */
    public class ArrayReversalDemo {

        public static void main(String[] args) {
            int[] numbers = {1, 2, 3, 4, 5, 6, 7};
            reverse(numbers);
        }

        /**
         * reverse the given array in place * @param input
         */
        public static void reverse(int[] input) {
            System.out.println("original array : " + Arrays.toString(input));
            // handling null, empty and one element array
            if (input == null || input.length <= 1) {
                return;
            }
            for (int i = 0; i < input.length / 2; i++) {
                int temp = input[i];
                // swap numbers
                input[i] = input[input.length - 1 - i];
                input[input.length - 1 - i] = temp;
            }
            System.out.println("reversed array : " + Arrays.toString(input));
        }
    }




Output:

    original array:[1,2,3,4,5,6,7]
    reversed array:[7,6,5,4,3,2,1]
    original array:[]
    original array:null
    original array:[1,2,3,4,5,6]
    reversed array:[6,5,4,3,2,1]
    original array:[1]
    reversed array:[1]


Ниже мой набор JUnit тестов для нашего `reverse(int[] input)` метода. Наши тесты должны покрывать случаи, когда массив пустой, когда вместо массива `null`, массив содержит один элемент, массив имеет четное и нечетное количество элементов.


    :::java
    import org.junit.Test;

    import static org.junit.Assert.assertArrayEquals;

    public class ArrayReversalDemoTest {
        @Test
        public void testReverseWithEvenLengthOfArray() {
            int[] numbers = {1, 2, 3, 4, 5, 6};
            ArrayReversalDemo.reverse(numbers);
            assertArrayEquals(new int[]{6, 5, 4, 3, 2, 1}, numbers);
        }

        @Test
        public void testReverseWithOddLengthOfArray() {
            int[] numbers = {1, 2, 3, 4, 5, 6, 7};
            ArrayReversalDemo.reverse(numbers);
            assertArrayEquals(new int[]{7, 6, 5, 4, 3, 2, 1}, numbers);
        }

        @Test
        public void testReverseWithEmptyArray() {
            int[] numbers = {};
            ArrayReversalDemo.reverse(numbers);
            assertArrayEquals(new int[]{}, numbers);
        }

        @Test
        public void testReverseWithNullArray() {
            int[] numbers = null;
            ArrayReversalDemo.reverse(numbers);
            assertArrayEquals(null, numbers);
        }

        @Test
        public void testReverseWithJustOneElementArray() {
            int[] numbers = {1};
            ArrayReversalDemo.reverse(numbers);
            assertArrayEquals(new int[]{1}, numbers);
        }
    }


Пока все. Продолжение следует...




