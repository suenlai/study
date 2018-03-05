[bits 16]
start:
	  mov ax,0123H
	  mov bx,0456H
	  add ax,bx
	  add ax,ax
	  mov ax,4c00h
	  int 21H
