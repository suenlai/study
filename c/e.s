	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 13
	.globl	_swap1
	.p2align	4, 0x90
_swap1:                                 ## @swap1
	.cfi_startproc
## BB#0:
	pushq	%rbp
Lcfi0:
	.cfi_def_cfa_offset 16
Lcfi1:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Lcfi2:
	.cfi_def_cfa_register %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movq	-8(%rbp), %rsi
	movl	(%rsi), %eax
	movl	%eax, -20(%rbp)
	movq	-16(%rbp), %rsi
	movl	(%rsi), %eax
	movq	-8(%rbp), %rsi
	movl	%eax, (%rsi)
	movl	-20(%rbp), %eax
	movq	-16(%rbp), %rsi
	movl	%eax, (%rsi)
	popq	%rbp
	retq
	.cfi_endproc

	.globl	_swap2
	.p2align	4, 0x90
_swap2:                                 ## @swap2
	.cfi_startproc
## BB#0:
	pushq	%rbp
Lcfi3:
	.cfi_def_cfa_offset 16
Lcfi4:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Lcfi5:
	.cfi_def_cfa_register %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movq	-8(%rbp), %rsi
	movq	%rsi, -24(%rbp)
	movq	-16(%rbp), %rsi
	movq	%rsi, -32(%rbp)
	movq	-24(%rbp), %rsi
	movq	(%rsi), %rsi
	movq	%rsi, -40(%rbp)
	movq	-32(%rbp), %rsi
	movq	(%rsi), %rsi
	movq	-24(%rbp), %rdi
	movq	%rsi, (%rdi)
	movq	-40(%rbp), %rsi
	movq	-32(%rbp), %rdi
	movq	%rsi, (%rdi)
	popq	%rbp
	retq
	.cfi_endproc

	.globl	_main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## BB#0:
	pushq	%rbp
Lcfi6:
	.cfi_def_cfa_offset 16
Lcfi7:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Lcfi8:
	.cfi_def_cfa_register %rbp
	subq	$48, %rsp
	leaq	L_.str(%rip), %rdi
	leaq	-12(%rbp), %rax
	leaq	-8(%rbp), %rcx
	movl	$0, -4(%rbp)
	movl	$10, -8(%rbp)
	movl	$20, -12(%rbp)
	movq	%rcx, -24(%rbp)
	movq	%rax, -32(%rbp)
	movq	-24(%rbp), %rax
	movl	(%rax), %esi
	movq	-32(%rbp), %rax
	movl	(%rax), %edx
	movb	$0, %al
	callq	_printf
	leaq	-32(%rbp), %rcx
	leaq	-24(%rbp), %rdi
	movq	%rcx, %rsi
	movl	%eax, -36(%rbp)         ## 4-byte Spill
	callq	_swap2
	leaq	L_.str(%rip), %rdi
	movq	-24(%rbp), %rcx
	movl	(%rcx), %esi
	movq	-32(%rbp), %rcx
	movl	(%rcx), %edx
	movb	$0, %al
	callq	_printf
	xorl	%edx, %edx
	movl	%eax, -40(%rbp)         ## 4-byte Spill
	movl	%edx, %eax
	addq	$48, %rsp
	popq	%rbp
	retq
	.cfi_endproc

	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"a=%i,b=%i\n"


.subsections_via_symbols
