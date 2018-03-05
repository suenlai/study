import java.util.stream.*;
import java.util.*;
public class StreamTest{
	public static void main(String[] args) {
	String[] list = {"program", "creek", "program", "creek", "java", "web",
            "program"};
    List<String> result = Stream.of(list)
            //.parallel()
            .filter(e -> e.length() >= 3)
            .map(e -> e.charAt(0))
            //.peek(System.out :: println)
            //.sorted()
            //.peek(e -> System.out.println("++++" + e))
            .map(e -> String.valueOf(e))
            .collect(Collectors.toList());
    System.out.println("----------------------------");
    System.out.println(result);
}
public static int sum(int a,int b){
	return a+b;
}
}
