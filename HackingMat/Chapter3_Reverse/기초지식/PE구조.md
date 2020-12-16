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


## IMAGE_DOS_HEADER (����ü ũ�� : 0x40 == 64byte)
�ش� ����ü�� �ִ� �ʵ��� ���� : 19��<br>
�� �� e_magic�ʵ�� e_lfanew �ʵ尡 �߿��ϴ�.<br>

### #e_magic (4D 5A)
PE �������� üũ��.<br>
EP(Entry Point)�κк��� 2����Ʈ�� �����ϸ�, 4D 5A ���� ������ ����.<br>
IMAZE_DOS_SIGNATURE�� ���Ͽ� �ٸ��� PE ���� ������ �ƴ϶�� ��.<br><br>

### #e_lfanew
IMAGE_NT_HEADER�� �������� ����<br>
�������� ���� ����<br>
NT ����� �ּҴ� ���� ����� e_lfanew�ʵ带 �����Ͽ� �˾� �� �� �ִٴ� ����.<br><br>

## Stub Code
���� ������� e_lfanew�� ũ�Ⱑ �������� ������ Stub Code ���� ������.<br>
Stub Code�� ���� �Ű� �Ƚᵵ ��<br>

## IMAGE_NT_HEADER
3���� �ʵ带 ���ϰ� ����<br>
> DWORD Signature;<br>
> IMAGE_FILE_HEADER FileHeader;<br>
> IMAGE_OPTIONAL_HEADER32 OptionalHeader;<br>

[IMAGE_NT_HEADER ����ü Ȯ��](https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image_nt_headers32)<br><br>


### #Signature (DWORD == 4byte)
PE �����ΰ��� üũ��.<br>
��� �״�� PE 00 �̶�� ���� ������, ��簪���� 50 45 00 00�� ����<br>
IMAGE_DOS_HEADER�� e_magic �κа� IMAGE_NT_HEADER�� Signature�� ���� ������ �����Ͽ� �����ϸ� ������<br>
FileHeader �ʵ�� OptionalHeader �ʵ�� ����ü �����̴� ����ü �м��� ��.<br>

## IMAGE_FILE_HEADER
PE ������ �⺻���� ������ �������.<br><br>
> WORD    Machine;<br>
> WORD    NumberOfSections;<br>
> DWORD   TimeDateStamp;<br>
> DWORD   PointerToSymbolTable;<br>
> DWORD   NumberOfSymbols;<br>
> WORD    SizeOfOptionalHeader;<br>
> WORD    Characteristics;<br>

[IMAGE_FILE_HEADER ����ü Ȯ��](https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image_file_header)<br><br>

### #Machine
������ � CPU���� ������ �� �ִ��� ������ �� �ִ� CPU�� Ÿ���� ����.<br>
whinnt.h�� ���ǵ� Machine ���.<br>
![Machine�� ��� ��](../imgs/PE����/Machine_�����.PNG)<br>
[�ڷ� ��ó](https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image_file_header)<br>
�� �̿ܿ��� �� ����.<br>
> \#define IMAGE_FILE_MACHINE_UNKNOWN           0 <br>
> \#define IMAGE_FILE_MACHINE_I386              0x014c  // Intel 386.<br>
> \#define IMAGE_FILE_MACHINE_R3000             0x0162  // MIPS little-endian, 0x160 big-endian<br>
> \#define IMAGE_FILE_MACHINE_R4000             0x0166  // MIPS little-endian<br>
> \#define IMAGE_FILE_MACHINE_R10000            0x0168  // MIPS little-endian<br>
> \#define IMAGE_FILE_MACHINE_WCEMIPSV2         0x0169  // MIPS little-endian WCE v2<br>
> \#define IMAGE_FILE_MACHINE_ALPHA             0x0184  // Alpha_AXP<br>
> \#define IMAGE_FILE_MACHINE_SH3               0x01a2  // SH3 little-endian<br>
> \#define IMAGE_FILE_MACHINE_SH3DSP            0x01a3<br>
> \#define IMAGE_FILE_MACHINE_SH3E              0x01a4  // SH3E little-endian<br>
> \#define IMAGE_FILE_MACHINE_SH4               0x01a6  // SH4 little-endian<br>
> \#define IMAGE_FILE_MACHINE_SH5               0x01a8  // SH5<br>
> \#define IMAGE_FILE_MACHINE_ARM               0x01c0  // ARM Little-Endian<br>
> \#define IMAGE_FILE_MACHINE_THUMB             0x01c2  // ARM Thumb/Thumb-2 Little-Endian<br>
> \#define IMAGE_FILE_MACHINE_ARMNT             0x01c4  // ARM Thumb-2 Little-Endian<br>
> \#define IMAGE_FILE_MACHINE_AM33              0x01d3<br>
> \#define IMAGE_FILE_MACHINE_POWERPC           0x01F0  // IBM PowerPC Little-Endian<br>
> \#define IMAGE_FILE_MACHINE_POWERPCFP         0x01f1<br>
> \#define IMAGE_FILE_MACHINE_IA64              0x0200  // Intel 64<br>
> \#define IMAGE_FILE_MACHINE_MIPS16            0x0266  // MIPS<br>
> \#define IMAGE_FILE_MACHINE_ALPHA64           0x0284  // ALPHA64<br>
> \#define IMAGE_FILE_MACHINE_MIPSFPU           0x0366  // MIPS<br>
> \#define IMAGE_FILE_MACHINE_MIPSFPU16         0x0466  // MIPS<br>
> \#define IMAGE_FILE_MACHINE_AXP64             IMAGE_FILE_MACHINE_ALPHA64<br>
> \#define IMAGE_FILE_MACHINE_TRICORE           0x0520  // Infineon<br>
> \#define IMAGE_FILE_MACHINE_CEF               0x0CEF<br>
> \#define IMAGE_FILE_MACHINE_EBC               0x0EBC  // EFI Byte Code<br>
> \#define IMAGE_FILE_MACHINE_AMD64             0x8664  // AMD64 (K8)<br>
> \#define IMAGE_FILE_MACHINE_M32R              0x9041  // M32R little-endian<br>
> \#define IMAGE_FILE_MACHINE_CEE               0xC0EE<br>
[�ڷ� ��ó](https://unabated.tistory.com/entry/PEPortable-Executable-����)<br>

### #NumberOfSections
PE ������ �ڵ�, ������, ���ҽ� ���� ������ ���ǿ� ����� �����.<br>
NumberOfSections�� �ٷ� �� ������ ������ ��Ÿ��.<br>
���� �ݵ�� 0���� Ŀ�� ��<br>
���ǵ� ���� ������ ���� ������ �ٸ��� ���� ������ �߻�<br>

### #SizeOfOptionalHeader
SizeOfOptionalHeader�� �ʵ忡�� IMAGE_OPTIONAL_HEADER32�� ũ�Ⱑ ���.<br>
IMAGE_OPTIONAL_HEADER32 ����ü�� ũ��� ������ ������, �ü������ ũ�Ⱑ �������̱⿡ PE�δ��� SizeOfOptionalHeader �ʵ��� ���� Ȯ���Ͽ�<br>
IMAGE_OPTIONAL_HEADER �� ũ�⸦ ó����.<br>
PE32+ ������ ������ ��� IMAGE_OPTIONAL_HEADER64 ����ü�� �����.<br>

> IMAGE_DOS_HEADER�� e_lfanew ����� IMAGE_FILE_HEADER�� SizeOfOptionalHeader ��� ������ �Ϲ����� PE ���� ������ ����� �ϸ� '�ʹ��' PE ����(PE Patch)�� ���� �� �ִٰ� ��.<br>