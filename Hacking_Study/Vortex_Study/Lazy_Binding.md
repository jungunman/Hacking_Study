# Lazy_binding
> Dynamic Linking 방식으로 컴파일이 된 ELF 바이너리는 공유 라이브러리 내에 위치한 함수의 주소를 동적으로 알아오기 위해 GOT(Global Offset Table) 테이블을 이용합니다.
> 함수 호출 시점에 해당 함수의 주소만 공유 라이브러리로부터 알아오는 것을 Lazy Binding이라고 한다.<br>
<br>
Lazy Binding을 사용하는 이유는 , Static 방식으로 컴파일하면 라이브러리의 모든 코드가 포함되서 용량이커진다. <br>
동일한 라이브러리를 사용하더라도 해당 라이브러리를 사용하는 모든 프로그램들은 라이브러리의 내용을 메모리에 매핑시켜야 하는 단점이 있다.<br>
그에 반에 Lazy Binding을 사용하면, 실행 시점에 필요한 함수의 주소만 알아오면 되기에, 실행 파일의 크기가 작고<br>
상대적으로 적은 메모리를 차지하게 되서 실행 속도도 빠르다.<br>

[Lazy Binding 및 GOT, RELRO - 참고문서](https://blackperl-security.gitlab.io/blog/2016/05/02/2016-05-02-linux-02/)<br>


### GOT overwrite란?
GOT는 PLT(Procedure Linkage Table)가 참조하는 테이블.프로시저들의 주소가 들어있다.<br>
즉 GOT를 조작하면 호출하려는 함수 대신 다른 함수를 호출 할 수 있다.
[GOT_Overwrite - 참고문서](https://nogadaworks.tistory.com/144)<br>


### Procedure란?
C언어에서 함수와 비슷한 개념으로, 차이점은 함수는 리턴 값을 남기지만 프로시저는 리턴 값을 남기지 않는다.
함수는 input값에 의한 output이 반드시 정의(void 제외)되야하나, 프로시저는 그렇지 않다.
[PLT GOT Procedure - 참고문서](https://bnzn2426.tistory.com/27)<br>
