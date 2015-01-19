title: "Снятие скриншотов с помощью WebDriver"
date: 2014-01-06 18:55:57 +0400
categories: selenium webdriver autotesting

Снятие скриншотов достаточно простая задача. В селениуме есть интерфейс TakesScreenshot который предоставляет возможность делать скриншоты веб-странницы. 

	:::java

	import java.io.File;
	import org.apache.commons.io.FileUtils;

	import org.openqa.selenium.WebDriver;
	import org.openqa.selenium.firefox.FirefoxDriver;
	import org.openqa.selenium.By;
	import org.openqa.selenium.OutputType;
	import org.openqa.selenium.TakesScreenshot;
	import org.openqa.selenium.WebElement;

	import org.junit.After;
	import org.junit.Before;
	import org.junit.Test;

	public class ScreenshotTests {
		
		WebDriver driver;
		
		@Before
		public void setUp()
		{
			driver = new FirefoxDriver();
			driver.get("http://www.google.com");
		}
	  
		@Test
		public void testTakesScreenshot()
		{
			try {
				File scrFile = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
				FileUtils.copyFile(scrFile, new File("c:\\scr\\main_page.png"));
		    } catch (Exception e) {
		        e.printStackTrace();
		    }
		}
	  
		
		@After
		public void teadDown()
		{
			driver.close();
			driver.quit();
		}
	  
	}