# PE (Portable Executable) ����
Windows ȯ���� ���� ���� ����.<br>
�ǽļ��� ������ �÷����� ������.<br>
Ȯ���� (SYS, DLL, SCR, OCX, OBJ ���)<br><br>

![PE����](../imgs/PE����/PE����.png)<br>
__*������ 16������ ũ�⸦ ������ ũ�⸦ ��Ÿ��*__

PE ����<br>
> DOS Header<br>
> Stub Code<br>
> PE Header(Optional, File Header)<br>
> Section Header(.text) == �ڵ带 �����ϴ� �ڵ� ����<br>
> Section Header(.data) == ���� ���� ���� ������ �����ϰ� �ִ� ������ ����<br>
> Section Header(.rsrc) == ���ڿ��̳� ������ ���� ���ҽ� �����͸� �����ϴ� ���ҽ� ����<br>
> Section Header(.reloc) == ���� ���Ͽ� ���� �⺻ ���ġ ������ ��� �ִ� ����<br>
> Padding == ���ǵ� ���̿� null(\x00)���� ��Ÿ���� �κ��� ���� ��Ģ�� ���� ũ�⸦ ������ ó�� ȿ���� ���̱� ���� ����ϴ� ����.<br>


