```
$ gcc inline_asm.c -o inline_asm
$ gdb -q ./inline_asm
Reading symbols from ./inline_asm...(no debugging symbols found)...done.
(gdb) i func
All defined functions:

Non-debugging symbols:
0x0000000100000000  _mh_execute_header
0x0000000100000f80  main
(gdb) disas main
Dump of assembler code for function main:
   0x0000000100000f80 <+0>:	push   %rbp
   0x0000000100000f81 <+1>:	mov    %rsp,%rbp
   0x0000000100000f84 <+4>:	mov    $0x0,%eax
   0x0000000100000f89 <+9>:	movl   $0x0,-0x4(%rbp)
   0x0000000100000f90 <+16>:	nop
   0x0000000100000f91 <+17>:	nop
   0x0000000100000f92 <+18>:	nop
   0x0000000100000f93 <+19>:	mov    %rax,%rax
   0x0000000100000f96 <+22>:	pop    %rbp
   0x0000000100000f97 <+23>:	retq   
End of assembler dump.
(gdb) q
$
```
