# FTZ-Hackschool
- setuid가 걸린 프로그램의 취약점을 이용하여, 권한을 얻어내 my-pass로 패스워드를 알아내는 방식이다.
- 기본적으로 필요한 지식 : 어셈블리어, Stack구조, EBP,ESP 작동방식, 리틀엔디언
- 다루면 좋은 도구 : gdb, c 언어, python, strace, vi, linux 기본 명령어(ls,cp,mkdir...)


## LittleEndian.py
- FTZ 문제를 풀다보면 주소를 알아내 리틀엔디언 방식으로 변환한 후, 페이로드에 작성해야하는 경우가 종종 있다.
- 처음에는 수작업으로 바꾸다가, 그냥 소스 코드로 만들었다.

## 쉘코드 모음 참고 블로그
- 쉘코드를 직접 만들 수 있으나, 기존에 있는 것으로 하는 것이 편하다.
- 참고 문서 : https://blog.kimtae.xyz/28

## BOF.md
- BufferOverFlow에 대한 기초 개념을 정리하는 곳이다.<br>
지속적인 업데이트로 완성시킬 예정.

## EGGSHELL.md
- EGGShell의 코드를 담아뒀다. <br>
뿐만 아니라, 실행 후 정확한 주소를 얻어내는 코드도 담아뒀다.