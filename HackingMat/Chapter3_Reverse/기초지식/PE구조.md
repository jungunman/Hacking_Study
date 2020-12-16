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


## IMAGE_DOS_HEADER (구조체 크기 : 0x40 == 64byte)
해당 구조체에 있는 필드의 갯수 : 19개<br>
그 중 e_magic필드와 e_lfanew 필드가 중요하다.<br>

### #e_magic (4D 5A)
PE 파일인지 체크함.<br>
EP(Entry Point)부분부터 2바이트를 차지하며, 4D 5A 값을 가지고 있음.<br>
IMAZE_DOS_SIGNATURE와 비교하여 다르면 PE 파일 구조가 아니라고 함.<br><br>

### #e_lfanew
IMAGE_NT_HEADER의 오프셋을 가짐<br>
가변적인 값을 지님<br>
NT 헤더의 주소는 도스 헤더의 e_lfanew필드를 참조하여 알아 낼 수 있다는 뜻임.<br><br>

## Stub Code
도스 헤더에서 e_lfanew의 크기가 가변적인 이유가 Stub Code 영역 떄문임.<br>
Stub Code는 딱히 신경 안써도 됨<br>

## IMAGE_NT_HEADER
3개의 필드를 지니고 있음<br>
> DWORD Signature;<br>
> IMAGE_FILE_HEADER FileHeader;<br>
> IMAGE_OPTIONAL_HEADER32 OptionalHeader;<br>

[IMAGE_NT_HEADER 구조체 확인](https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image_nt_headers32)<br><br>


### #Signature (DWORD == 4byte)
PE 파일인가를 체크함.<br>
상수 그대로 PE 00 이라는 값을 가지며, 헥사값으로 50 45 00 00의 값임<br>
IMAGE_DOS_HEADER의 e_magic 부분과 IMAGE_NT_HEADER의 Signature를 임의 값으로 수정하여 실행하면 오류남<br>
FileHeader 필드와 OptionalHeader 필드는 구조체 형식이니 구조체 분석에 들어감.<br>

## IMAGE_FILE_HEADER
PE 파일의 기본적인 내용이 담겨있음.<br><br>
> WORD    Machine;<br>
> WORD    NumberOfSections;<br>
> DWORD   TimeDateStamp;<br>
> DWORD   PointerToSymbolTable;<br>
> DWORD   NumberOfSymbols;<br>
> WORD    SizeOfOptionalHeader;<br>
> WORD    Characteristics;<br>

[IMAGE_FILE_HEADER 구조체 확인](https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image_file_header)<br><br>

### #Machine
파일이 어떤 CPU에서 동작할 수 있는지 실행할 수 있는 CPU의 타입을 정함.<br>
whinnt.h에 정의된 Machine 상수.<br>
![Machine의 상수 값](../imgs/PE구조/Machine_상수값.PNG)<br>
[자료 출처](https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image_file_header)<br>
이 이외에도 더 있음.<br>
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
[자료 출처](https://unabated.tistory.com/entry/PEPortable-Executable-구조)<br>

### #NumberOfSections
PE 파일은 코드, 데이터, 리소스 등이 각각의 섹션에 나뉘어서 저장됨.<br>
NumberOfSections는 바로 그 섹션의 개수를 나타냄.<br>
값이 반드시 0보다 커야 함<br>
정의된 섹션 개수와 실제 섹션이 다르면 실행 에러가 발생<br>

### #SizeOfOptionalHeader
SizeOfOptionalHeader의 필드에는 IMAGE_OPTIONAL_HEADER32의 크기가 담김.<br>
IMAGE_OPTIONAL_HEADER32 구조체의 크기는 정해져 있지만, 운영체제마다 크기가 가변적이기에 PE로더가 SizeOfOptionalHeader 필드의 값을 확인하여<br>
IMAGE_OPTIONAL_HEADER 의 크기를 처리함.<br>
PE32+ 형태의 파일의 경우 IMAGE_OPTIONAL_HEADER64 구조체를 사용함.<br>

> IMAGE_DOS_HEADER의 e_lfanew 멤버와 IMAGE_FILE_HEADER의 SizeOfOptionalHeader 멤버 때문에 일반적인 PE 파일 형식을 벗어나는 일명 '꽈배기' PE 파일(PE Patch)을 만들 수 있다고 함.<br>