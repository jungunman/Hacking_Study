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
�׷����� ���� ���ƿԴ�.
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
big = struct.unpack('<I', data)[0] #���� �� ��Ʋ ����� ��ȯ

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
���� ����� �̷���.

![struct_Little_Endian](./imgs/level0/4.png)

#### �� == _Username: vortex1 Password: Gq#qu3bF3_ 
