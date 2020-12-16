# PE (Portable Executable) 구조
Windows 환경의 실행 파일 포맷.<br>
의식성이 있으면 플랫폼에 독립적.<br>
확장자 (SYS, DLL, SCR, OCX, OBJ 등등)<br><br>

![PE구조](../imgs/PE구조/PE구조.png)<br>
__*왼쪽의 16진수는 크기를 섹션의 크기를 나타냄*__

PE 순서<br>
> DOS Header<br>
> Stub Code<br>
> PE Header(Optional, File Header)<br>
> Section Header(.text) == 코드를 포함하는 코드 섹션<br>
> Section Header(.data) == 전역 변수 정적 변수를 포함하고 있는 데이터 섹션<br>
> Section Header(.rsrc) == 문자열이나 아이콘 같은 리소스 데이터를 포함하는 리소스 섹션<br>
> Section Header(.reloc) == 실행 파일에 대한 기본 재배치 정보를 담고 있는 섹션<br>
> Padding == 섹션들 사이에 null(\x00)으로 나타나는 부분은 정렬 규칙에 의해 크기를 버리고 처리 효유을 높이기 위해 사용하는 영역.<br>


