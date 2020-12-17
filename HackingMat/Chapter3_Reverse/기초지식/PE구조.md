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



### #Machine
������ � CPU���� ������ �� �ִ��� ������ �� �ִ� CPU�� Ÿ���� ����.<br>
whinnt.h�� ���ǵ� Machine ���.<br>
![Machine�� ��� ��](../imgs/PE����/Machine_�����.PNG)<br>

�� �̿ܿ��� �� ����.<br>
```C
#define IMAGE_FILE_MACHINE_UNKNOWN           0 
#define IMAGE_FILE_MACHINE_I386              0x014c  // Intel 386.
#define IMAGE_FILE_MACHINE_R3000             0x0162  // MIPS little-endian, 0x160 big-endian
#define IMAGE_FILE_MACHINE_R4000             0x0166  // MIPS little-endian
#define IMAGE_FILE_MACHINE_R10000            0x0168  // MIPS little-endian
#define IMAGE_FILE_MACHINE_WCEMIPSV2         0x0169  // MIPS little-endian WCE v2
#define IMAGE_FILE_MACHINE_ALPHA             0x0184  // Alpha_AXP
#define IMAGE_FILE_MACHINE_SH3               0x01a2  // SH3 little-endian
#define IMAGE_FILE_MACHINE_SH3DSP            0x01a3
#define IMAGE_FILE_MACHINE_SH3E              0x01a4  // SH3E little-endian
#define IMAGE_FILE_MACHINE_SH4               0x01a6  // SH4 little-endian
#define IMAGE_FILE_MACHINE_SH5               0x01a8  // SH5
#define IMAGE_FILE_MACHINE_ARM               0x01c0  // ARM Little-Endian
#define IMAGE_FILE_MACHINE_THUMB             0x01c2  // ARM Thumb/Thumb-2 Little-Endian
#define IMAGE_FILE_MACHINE_ARMNT             0x01c4  // ARM Thumb-2 Little-Endian
#define IMAGE_FILE_MACHINE_AM33              0x01d3
#define IMAGE_FILE_MACHINE_POWERPC           0x01F0  // IBM PowerPC Little-Endian
#define IMAGE_FILE_MACHINE_POWERPCFP         0x01f1
#define IMAGE_FILE_MACHINE_IA64              0x0200  // Intel 64
#define IMAGE_FILE_MACHINE_MIPS16            0x0266  // MIPS
#define IMAGE_FILE_MACHINE_ALPHA64           0x0284  // ALPHA64
#define IMAGE_FILE_MACHINE_MIPSFPU           0x0366  // MIPS
#define IMAGE_FILE_MACHINE_MIPSFPU16         0x0466  // MIPS
#define IMAGE_FILE_MACHINE_AXP64             IMAGE_FILE_MACHINE_ALPHA64
#define IMAGE_FILE_MACHINE_TRICORE           0x0520  // Infineon
#define IMAGE_FILE_MACHINE_CEF               0x0CEF
#define IMAGE_FILE_MACHINE_EBC               0x0EBC  // EFI Byte Code
#define IMAGE_FILE_MACHINE_AMD64             0x8664  // AMD64 (K8)<br>8t67
#define IMAGE_FILE_MACHINE_M32R              0x9041  // M32R little-endian
#define IMAGE_FILE_MACHINE_CEE               0xC0EE
```


### #NumberOfSections
PE ������ �ڵ�, ������, ���ҽ� ���� ������ ���ǿ� ����� �����.<br>
NumberOfSections�� �ٷ� �� ������ ������ ��Ÿ��.<br>
���� �ݵ�� 0���� Ŀ�� ��<br>
���ǵ� ���� ������ ���� ������ �ٸ��� ���� ������ �߻�<br>

### #SizeOfOptionalHeader
SizeOfOptionalHeader�� �ʵ忡�� IMAGE_OPTIONAL_HEADER32�� ũ�Ⱑ ���.<br>
IMAGE_OPTIONAL_HEADER32 ����ü�� ũ��� ������ ������, �ü������ ũ�Ⱑ �������̱⿡<br>
PE�δ��� SizeOfOptionalHeader �ʵ��� ���� Ȯ���Ͽ� IMAGE_OPTIONAL_HEADER �� ũ�⸦ ó����.<br>
PE32+ ������ ������ ��� IMAGE_OPTIONAL_HEADER64 ����ü�� �����.<br>

> IMAGE_DOS_HEADER�� e_lfanew ����� IMAGE_FILE_HEADER�� SizeOfOptionalHeader ��� ������ �Ϲ����� PE ���� ������ ����� �ϸ� '�ʹ��' PE ����(PE Patch)�� ���� �� �ִٰ� ��.<br>

### #Characteristics
���� ������ ������ �˷��ִ� ����.<br>
���� ������ ��������, DLL ��������, �ý��� ��������, ���ġ ���ε ���� ������ ������ ����.<br>

__*Characteristics �ʵ� ���*__ <br>
```C
#define IMAGE_FILE_RELOCS_STRIPPED           0x0001  // Relocation info stripped from file.
#define IMAGE_FILE_LINE_NUMS_STRIPPED        0x0004  // Line nunbers stripped from file.
#define IMAGE_FILE_LOCAL_SYMS_STRIPPED       0x0008  // Local symbols stripped from file.
#define IMAGE_FILE_AGGRESIVE_WS_TRIM         0x0010  // Agressively trim working set
#define IMAGE_FILE_LARGE_ADDRESS_AWARE       0x0020  // App can handle >2gb addresses
#define IMAGE_FILE_BYTES_REVERSED_LO         0x0080  // Bytes of machine word are reversed.
#define IMAGE_FILE_32BIT_MACHINE             0x0100  // 32 bit word machine.
#define IMAGE_FILE_DEBUG_STRIPPED            0x0200  // Debugging info stripped from file in .DBG file
#define IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP   0x0400  // If Image is on removable media, copy and run from the swap file.
#define IMAGE_FILE_NET_RUN_FROM_SWAP         0x0800  // If Image is on Net, copy and run from the swap file.
#define IMAGE_FILE_SYSTEM                    0x1000  // System File.
#define IMAGE_FILE_DLL                       0x2000  // File is a DLL.
#define IMAGE_FILE_UP_SYSTEM_ONLY            0x4000  // File should only be run on a UP machine
#define IMAGE_FILE_BYTES_REVERSED_HI         0x8000  // Bytes of machine word are reversed.
```

### #TimeDateStamp
PE ������ ������� �ð�.<br>
������ ����� ��¥�� Ÿ�ӽ����� �������� ���<br>
������ ������ �ŷ��� ���� �ƴϴ�.<br>


## IMAGE_OPTIONAL_HEADER (PE ����ü�� ���� ŭ)
31���� �ʵ带 ������ ����<br>
�� �� �߿��� �Ϻθ� ���캸��, �ʿ��ϸ� �� ������ ��.<br>


```C
typedef struct _IMAGE_DATA_DIRECTORY {
    DWORD   VirtualAddress;
    DWORD   Size;
} IMAGE_DATA_DIRECTORY, *PIMAGE_DATA_DIRECTORY;
 
typedef struct _IMAGE_OPTIONAL_HEADER {
    WORD    Magic;
    BYTE    MajorLinkerVersion;
    BYTE    MinorLinkerVersion;
    DWORD   SizeOfCode;
    DWORD   SizeOfInitializedData;
    DWORD   SizeOfUninitializedData;
    DWORD   AddressOfEntryPoint;
    DWORD   BaseOfCode;
    DWORD   BaseOfData;
    DWORD   ImageBase;
    DWORD   SectionAlignment;
    DWORD   FileAlignment;
    WORD    MajorOperatingSystemVersion;
    WORD    MinorOperatingSystemVersion;
    WORD    MajorImageVersion;
    WORD    MinorImageVersion;
    WORD    MajorSubsystemVersion;
    WORD    MinorSubsystemVersion;
    DWORD   Win32VersionValue;
    DWORD   SizeOfImage;
    DWORD   SizeOfHeaders;
    DWORD   CheckSum;
    WORD    Subsystem;
    WORD    DllCharacteristics;
    DWORD   SizeOfStackReserve;
    DWORD   SizeOfStackCommit;
    DWORD   SizeOfHeapReserve;
    DWORD   SizeOfHeapCommit;
    DWORD   LoaderFlags;
    DWORD   NumberOfRvaAndSizes;
    IMAGE_DATA_DIRECTORY DataDirectory[IMAGE_NUMBEROF_DIRECTORY_ENTRIES];
} IMAGE_OPTIONAL_HEADER32, *PIMAGE_OPTIONAL_HEADER32;
```


### #Magic
PE ������ 10B�� ���� ������ PE+������ 20B��� ���� ����.<br>


### #SizeOfCode
�ڵ� ������ ��ü ũ�Ⱑ �̰��� ��.<br>
.text ������ ũ�Ⱑ ��.<br>
SizeOfcode�� Section Header(.text)�� ũ�Ⱑ ��ġ�ϴ��� ������<br><br>

### #ImageBase
PE ������ �޸𸮿� �ε�� ���� ���� �ּ�.<br>
���μ����� ���� �޸𸮴� 0~FFFFFFFF ������(32bit ���), �� ��������<br>
EXE,DLL�� user memory ������ 0~7FFFFFFF ������ �ε��� �ǰ�,<br>
SYS. ������ kernel memory ������ 80000000~FFFFFFFF ������ �ε���.<br>
�Ϲ������� EXE ������ ImageBase ���� 00400000�̰�,<br>
DLL������ ImageBase ���� 10000000��.<br>
���� �� ����, �� �ּҰ� �ƴ� ��Ŀ �ɼ��� ���ؼ� �ٸ� ���� �ּҷ� �ٲ� �� ����.<br>
_PE �δ��� P ������ �����Ű�� ���� ���μ����� �����ϰ� ������ �޸𸮿� �ε����� EIP �������� ���� ImageBase + AddressOfEntryPoint ������ �����Ѵ�._

### #AddressOFEntryPoint
���α׷��� �޸𸮿��� ����Ǵ� ���� ����, EP(EntryPoint)�� RVA(Relative Virtual Address) ���� ������ ����.<br>

> VA(Virtual Address) == ���μ��� ���� �޸��� ���� �ּ�<br>
> RVA(Relative Virtual Address) == ��� ���� ��ġ(ImageBase)���� ������ ����ּ�<br>
> RVA + ImageBase == VA<br>

### #BaseOfCode
�ڵ� ������ ���۵Ǵ� RVA(��� �ּ�)�� ������ ����.<br>
BaseOfCode + ImageBase == ���� �ڵ� ������ �ּ���.<br><br>

### #SelectionAlignment, FileAlignment
PE ������ Body �κ��� Section���� �������� ����<br>
FileAlignment == ���Ͽ��� ������ �ּҴ���<br>
SelectionAlignment == �޸𸮿��� ������ �ּҴ���<br>
SelectionAlignment, FileAlignment �� ũ�Ⱑ ���� �� �ְ� �ٸ� ���� ����.<br>
���� / �޸��� ���� ũ��� �ݵ�� ����  FileAlignment / SelectionAlignment�� ����� �Ǿ�� ��.<br>
������� �е��������� ä����<br><br>

### #SizeOfImage
PE ������ �޸𸮿� �ε��Ǿ��� �� ��ü ũ�⸦ ��� ����.<br>
�Ϲ������� ������ ũ��� �޸𸮿� �ε��� ũ��� �ٸ�<br>
_�� ������ �ε� ��ġ�� �޸� ���� ũ��� ���� ����� ���ǵǾ� ����_<br><br>

### #SizeOfHeader
PE ����� ��ü ũ�⸦ ��Ÿ��<br>
�� �� ���� FileAlignment�� ������� ��.<br>
���� ���ۿ��� SizeOfHeader Offset ��ŭ ������ ��ġ�� ù ��° ������ ��ġ��.<br><br> 


### #Subsystem
�� �ʵ带 ���� �ý��� ����̹� ����(*.sys)����, �Ϲ� ���� ����(*.exe, *.dll)���� ������ �� ����.<br>
| �� | �ǹ� | ��� |
|:---:|:---:|:---:|
| 1 | Driver File | �ý��� ����̹�(��:ntfs.sys)|
| 2 | GUI(Graphic User Interface) ���� | â ��� ���ø����̼�(�� : notepad.exe)|
| 3 | CUI(Console User Interface) ���� | �ܼ� ��� ���ø����̼�(�� : cmd.exe)|

�� �̿ܿ��� OS2, POSIX, CE ��� ���� ����ý����� ����<br><br>

### #NumberOfRvaAndSizes
�� �ʵ�� IMAGE_OPTIONAL_HEADER32 ����ü�� ������ ����� DataDirectory �迭�� ������ ��Ÿ��.<br>
����ü ���ǿ� IMAGE_NUMBEROF_DIRECTORY_ENTRIES(16)�̶�� ��õǾ� ������,<br>
PE �δ��� �� �ʵ��� ���� ���� �迭�� ũ�⸦ �ν���<br>
��, 16�� �ƴ� ���� ����.<br><br>


### #DataDirectory
IMAGE_DATA_DIRECTORY ����ü�� �迭��, �迭�� �� �׸񸶴� ���ǵ� ���� ����.<br>

```C
#define IMAGE_DIRECTORY_ENTRY_EXPORT          0   // Export Directory
#define IMAGE_DIRECTORY_ENTRY_IMPORT          1   // Import Directory
#define IMAGE_DIRECTORY_ENTRY_RESOURCE        2   // Resource Directory
#define IMAGE_DIRECTORY_ENTRY_EXCEPTION       3   // Exception Directory
#define IMAGE_DIRECTORY_ENTRY_SECURITY        4   // Security Directory
#define IMAGE_DIRECTORY_ENTRY_BASERELOC       5   // Base Relocation Table
#define IMAGE_DIRECTORY_ENTRY_DEBUG           6   // Debug Directory
//      IMAGE_DIRECTORY_ENTRY_COPYRIGHT       7   // (X86 usage)
#define IMAGE_DIRECTORY_ENTRY_ARCHITECTURE    7   // Architecture Specific Data
#define IMAGE_DIRECTORY_ENTRY_GLOBALPTR       8   // RVA of GP
#define IMAGE_DIRECTORY_ENTRY_TLS             9   // TLS Directory
#define IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG    10   // Load Configuration Directory
#define IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT   11   // Bound Import Directory in headers
#define IMAGE_DIRECTORY_ENTRY_IAT            12   // Import Address Table
#define IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT   13   // Delay Load Import Descriptors
#define IMAGE_DIRECTORY_ENTRY_COM_DESCRIPTOR 14   // COM Runtime descriptor

```
IMAGE_OPTIONAL_HEADER�� DataDirectory �ʵ�� �ͽ���Ʈ ���͸�, ����Ʈ ���͸�, ���ҽ� ���͸�, ���� ���͸�, ���� ���͸� ���� � ������ �� �ִ� �ּҿ� ũ�⸦ ���ϰ� �ִ� �迭��,<br>
IMAGE_DATA_DIRECTORY ����ü�� VirtualAddress�� ���� ���� �ּҸ� �� �� ������, Size�� ���� ũ�⸦ �� �� ����.<br>
�߿��� ���� EXPORT, IMPORT, RESOURCE, TLS, IAT�̰� ���߿� �˾ƺ�����<br>






## �ڷ� ��ó ����
[PE ���� �ڷ� ��ó](https://unabated.tistory.com/entry/PEPortable-Executable-����)<br>
[IMAGE_FILE_HEADER ����ü ��ó](https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image_file_header)<br>
[IMAGE_NT_HEADER ����ü ��ó](https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image_nt_headers32)<br>