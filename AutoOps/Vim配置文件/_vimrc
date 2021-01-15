" -----------------------------------------------------------------------------
"  < Vundle 插件配置 >
" -----------------------------------------------------------------------------
set nocompatible        " be iMproved  
filetype off            " required
" 设置包括vundle和初始化相关的runtime path
" 判断操作系统类型
if(has('win32') || has('win64'))
    set rtp+=$VIM\vimfiles\bundle\Vundle.vim
    let path='$VIM\vimfiles\bundle'
else
    set rtp+=~/.vim/bundle/Vundle.vim
    let path='~/.vim/bundle'
endif
call vundle#begin(path)
" 另一种选择, 指定一个vundle安装插件的路径
"call vundle#begin('~/some/path/here')
" let Vundle manage Vundle
"Bundle 'gmarik/vundle'
Plugin 'VundleVim/Vundle.vim'
Plugin 'plytophogy/vim-virtualenv'
Plugin 'skywind3000/asyncrun.vim'
" My Bundles here:
" original repos on github
" github上的用户写的插件，使用这种用户名+repo名称的方式
" Bundle 'tpope/vim-fugitive'
" Bundle 'Lokaltog/vim-easymotion'
" Bundle 'rstacruz/sparkup', {'rtp': 'vim/'}
" Bundle 'tpope/vim-rails.git'
"1.PowerLine插件 状态栏增强展示
Bundle 'Lokaltog/vim-powerline'
    "vim有一个状态栏 加上powline则有两个状态栏
    set laststatus=2
    set t_Co=256
    let g:Powline_symbols='fancy'
Bundle 'majutsushi/tagbar'
    let g:tagbar_ctags_bin='ctags'          "ctags程序的路径
    let g:tagbar_width=30               "窗口宽度的设置
    nmap tl :Tagbar<CR>
Bundle 'fholgado/minibufexpl.vim'
    let g:miniBufExplMapWindowNavVim = 1   
    let g:miniBufExplMapWindowNavArrows = 1   
    let g:miniBufExplMapCTabSwitchBufs = 1   
    let g:miniBufExplModSelTarget = 1  
    let g:miniBufExplMoreThanOne=0
Bundle 'scrooloose/nerdtree'
map wm :NERDTreeMirror<CR>
map wm :NERDTreeToggle<CR>
" vim-scripts repos
" vimscripts的repo使用下面的格式，直接是插件名称
""Bundle 'L9'
"Bundle 'SuperTab'
"Bundle 'vimwiki'
"Bundle 'winmanager'
"Bundle 'bufexplorer.zip'
""Bundle 'The-NERD-Commenter'
"Bundle 'matrix.vim--Yang'
"Bundle 'FencView.vim'
"Bundle 'Conque-Shell'
"Bundle 'Vimpress'
Bundle 'Mark'
    " -----------------------------------------------------------------------------
    "  < Mark--Karkat（也就是 Mark 插件配置 >
    " 给不同的单词高亮，表明不同的变量时很有用，详细帮助见 :h mark.txt
    " -----------------------------------------------------------------------------
    set viminfo+=!                     " 保存全局变量
    let g:mwAutoSaveMarks = 1
    let g:mwAutoLoadMarks = 1
    nmap <F3> \*
"Bundle 'Markdown'
"Bundle 'LaTeX-Suite-aka-Vim-LaTeX'
Bundle 'a.vim'
Bundle 'Raimondi/delimitMate'
"Bundle 'snipMate'
" non github reposo
" 非github的插件，可以直接使用其git地址
" Bundle 'git://git.wincent.com/command-t.git'
" ...
"git interface
Plugin 'tpope/vim-fugitive'
"filesystem
""Plugin 'jistr/vim-nerdtree-tabs'
""Plugin 'kien/ctrlp.vim' 
"html
"  isnowfy only compatible with python not python3
""Plugin 'isnowfy/python-vim-instant-markdown'
Plugin 'jtratner/vim-flavored-markdown'
Plugin 'suan/vim-instant-markdown'
Plugin 'nelstrom/vim-markdown-preview'
"python sytax checker
Plugin 'nvie/vim-flake8'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'scrooloose/syntastic'
"auto-completion stuff
""Plugin 'klen/python-mode'
"Plugin 'Valloric/YouCompleteMe'
""Plugin 'klen/rope-vim'
""Plugin 'davidhalter/jedi-vim'
Plugin 'ervandew/supertab'
""code folding
Plugin 'tmhedberg/SimpylFold'
"Colors!!!
""Plugin 'altercation/vim-colors-solarized'
""Plugin 'jnurmine/Zenburn'
" 你的所有插件需要在下面这行之前
call vundle#end()            " 必须
filetype plugin indent on    " 必须 加载vim自带和插件相应的语法和文件类型相关脚本
" 忽视插件改变缩进,可以使用以下替代:
"filetype plugin on
" Brief help
" :BundleList          - list configured bundles
" :BundleInstall(!)    - install(update) bundles
" :BundleSearch(!) foo - search(or refresh cache first) for foo
" :BundleClean(!)      - confirm(or auto-approve) removal of unused bundles
" vundle主要就是上面这个四个命令，例如BundleInstall是全部重新安装，BundleInstall!则是更新
" 一般安装插件的流程为，先BundleSearch一个插件，然后在列表中选中，按i安装
" 安装完之后，在vimrc中，添加Bundle 'XXX'，使得bundle能够加载，这个插件，同时如果
" 需要配置这个插件，也是在vimrc中设置即可
" see :h vundle for more details or wiki for FAQ
" NOTE: comments after Bundle command are not allowed..
" 以下范例用来支持不同格式的插件安装.
" 请将安装插的命令放在vundle#begin和vundle#end之间.
" Github上的插件
" 格式为 Plugin '用户名/插件仓库名'
"Plugin 'tpope/vim-fugitive'
" 来自 http://vim-scripts.org/vim/scripts.html 的插件
" Plugin '插件名称' 实际上是 Plugin 'vim-scripts/插件仓库名' 只是此处的用户名可以省略
"Plugin 'L9'
" 由Git支持但不再github上的插件仓库 Plugin 'git clone 后面的地址'
"Plugin 'git://git.wincent.com/command-t.git'
" 本地的Git仓库(例如自己的插件) Plugin 'file:///+本地插件仓库绝对路径'
"Plugin 'file:///home/gmarik/path/to/plugin'
" 插件在仓库的子目录中.
" 正确指定路径用以设置runtimepath. 以下范例插件在sparkup/vim目录下
"Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" 避免插件名冲突,例如L9已存在,则可以指定
"Plugin 'user/L9', {'name': 'newL9'}
"
" 简要帮助文档
" :PluginList       - 列出所有已配置的插件
" :PluginInstall    - 安装插件,追加 `!` 用以更新或使用 :PluginUpdate
" :PluginSearch foo - 搜索 foo ; 追加 `!` 清除本地缓存
" :PluginClean      - 清除未使用插件,需要确认; 追加 `!` 自动批准移除未使用插件
"
" 查阅 :h vundle 获取更多细节和wiki以及FAQ
" 将你自己对非插件片段放在这行之后
"
"
"
set autochdir
source $VIMRUNTIME/vimrc_example.vim
source $VIMRUNTIME/mswin.vim 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set langmenu=zh_CN.UTF-8
language messages zh_CN.UTF-8
let &termencoding=&encoding
set fileencodings=utf-8,gbk,ucs-bom,cp936 
set encoding=utf-8
set fencs=utf-8,gb18030,gbk,gb2312,cp936,ucs-bom,euc-jp,
behave mswin
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set diffexpr=MyDiff()
function MyDiff()
  let opt = '-a --binary '
  if &diffopt =~ 'icase' | let opt = opt . '-i ' | endif
  if &diffopt =~ 'iwhite' | let opt = opt . '-b ' | endif
  let arg1 = v:fname_in
  if arg1 =~ ' ' | let arg1 = '"' . arg1 . '"' | endif
  let arg2 = v:fname_new
  if arg2 =~ ' ' | let arg2 = '"' . arg2 . '"' | endif
  let arg3 = v:fname_out
  if arg3 =~ ' ' | let arg3 = '"' . arg3 . '"' | endif
  let eq = ''
  if $VIMRUNTIME =~ ' '
    if &sh =~ '\<cmd'
      let cmd = '"' . $VIMRUNTIME . '\diff"'
      let eq = '""'
    else
      let cmd = substitute($VIMRUNTIME, ' ', '" ', '') . '\diff"'
    endif
  else
    let cmd = $VIMRUNTIME . '\diff'
  endif
 silent execute '!' . cmd . ' ' . opt . arg1 . ' ' . arg2 . ' > ' . arg3 . eq
endfunction
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"一般设定
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"gvim的字体设定
set guifont=Consolas:h13
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"不要使用vi的键盘模式，而是vim自己的
set nocompatible
"history文件中需要记录的行数
set history=100
"在处理未保存或只读文件的时候，弹出确认
set confirm
"与windows共享剪贴板
set clipboard+=unnamed
"侦测文件类型
filetype on
"载入文件类型插件
filetype plugin on
"为特定文件类型载入相关缩进文件
filetype indent on
"保存全局变量
set viminfo+=!
set viminfo='1000,f1,<100
"带有如下符号的单词不要被换行分割
set iskeyword+=_,$,@,%,#,-
"语法高亮
set nu!
syntax enable
syntax on
"color zenburn
"color desertEx
"colorscheme desert
"colo peachpuff 
colorscheme murphy
"高亮字符，让其不受100列限制
"":highlight OverLength ctermbg=red ctermfg=white guibg=red guifg=white
"":match OverLength '\%101v.*'
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"文件设置
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"不要备份文件（根据自己需要取舍）
set nobackup
"不要生成swap文件，当buffer被丢弃的时候隐藏它
setlocal noswapfile
set bufhidden=hide
"字符间插入的像素行数目
set linespace=0
"增强模式中的命令行自动完成操作
set wildmenu
"在状态行上显示光标所在位置的行号和列号
set ruler
set rulerformat=%20(%2*%<%f%=\ %m%r\ %3l\ %c\ %p%%%)
"命令行（在状态行下）的高度，默认为1，这里是2
set cmdheight=2
"使回格键（backspace）正常处理indent, eol, start等
set backspace=2
"可以在buffer的任何地方使用鼠标（类似office中在工作区双击鼠标定位）
set mouse=a
set selection=exclusive
set selectmode=mouse,key
"通过使用: commands命令，告诉我们文件的哪一行被改变过
set report=0
"在被分割的窗口间显示空白，便于阅读
set fillchars=vert:\ ,stl:\ ,stlnc:\
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"搜索和匹配
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"高亮显示匹配的括号
set showmatch
"匹配括号高亮的时（单位是十分之一秒）
set matchtime=5
"在搜索的时候忽略大小写
set ignorecase
"不要高亮被搜索的句子（phrases）
set nohlsearch
"在搜索时，输入的词句的逐字符高亮（类似firefox的搜索）
set incsearch
"光标移动到buffer的顶部和底部时保持3行距离
set scrolloff=3
"不要闪烁
set novisualbell
"我的状态行显示的内容（包括文件类型和解码）
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"我的状态行显示的内容（包括文件类型和解码）
""set statusline=%F%m%r%h%w\[POS=%l,%v][%p%%]\%{strftime(\"%Y-%m-%d\ \%H:%M\")}\ %{''.(&fenc!=''?&fenc:&enc).''}\ %{(&bomb?\",BOM\":\"\")}
"总是显示状态行
""set laststatus=2
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"文本格式和排版
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"自动格式化
set formatoptions=tcrqn
"继承前一行的缩进方式，特别适用于多行注释
set autoindent
"为C程序提供自动缩进
set smartindent
"使用C样式的缩进
set cindent
"制表符为4统一缩进为4
set tabstop=4
set softtabstop=4
set shiftwidth=4
"用空格代替制表符
set expandtab
"不要换行
set nowrap
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"不要显示折叠树
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"Autocommands
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"只在下列文件类型被侦测到的时候显示行号，普通文本文件不显示
if has("autocmd")
    autocmd FileType xml,html,c,cs,java,perl,shell,bash,cpp,python,vim,php,ruby set number
    autocmd FileType xml,html vmap <C-o> <ESC>'<i<!--<ESC>o<ESC>'>o-->
    autocmd FileType java,c,cpp,cs vmap <C-o> <ESC>'<o/*<ESC>'>o*/
    autocmd FileType html,text,php,vim,c,java,xml,bash,shell,perl,python setlocal textwidth=100
    autocmd Filetype html,xml,xsl source $VIMRUNTIME/plugin/closetag.vim
    autocmd BufReadPost *
      \ if line("'\"") > 0 && line("'\"") <= line("$") |
      \ exe " normal g`\"" |
      \ endif
endif "has("autocmd")
"F5编译和运行C程序，F6编译和运行C++程序
"请注意，下述代码在windows下使用会报错
"需要去掉./这两个字符
"去空行  
""nnoremap <F2> :g/^\s*$/d<CR> 
"C的编译和运行
map <F5> :call CompileRun()<CR>
func! CompileRun()
    exec "w"
    if &filetype == 'c'
        exec "!gcc % -o %<"
        exec "! ./%<"
    elseif &filetype == 'cpp'
        exec "!g++ % -o %<"
        exec "! ./%<"
    elseif &filetype == 'java'
        exec "!javac %"
        exec "!java %<"
    elseif &filetype == 'python'
        exec "!python %"
    endif
endfunc
map <F6> :call CompileOnly()<CR>
func! CompileOnly()
    exec "w"
    if &filetype == 'c'
        exec "AsyncRun gcc % -o %<"
    elseif &filetype == 'cpp'
        exec "AsyncRun g++ % -o %<"
    elseif &filetype == 'python'
        exec "AsyncRun python %" 
    endif 
endfunc
map <F7> :call RunAsync()<CR>
func! RunAsync()
    exec "w"
    if &filetype == 'c'
        exec "AsyncRun gcc % -o %<"
    elseif &filetype == 'cpp'
        exec "AsyncRun g++ % -o %<"
    elseif &filetype == 'python'
        exec "!start python %"
    endif 
endfunc
"高亮显示普通txt文件（需要txt.vim脚本）
au BufRead,BufNewFile * setfiletype txt
"映射<F11>的作用
map <F11> :call CallTags() <CR>
func! CallTags()
	exec "w"
	"exec "! ctags -R --c++-kinds=+p --fields=+iaS --extra=+q"
	exec "! ctags -R %"
	exec "set tags+=tags"
endfun
"新建.c,.h,.sh,.java文件，自动插入文件头 
autocmd BufNewFile *.c,*.sh,*.cpp,*.java,*.py exec ":call SetTitle()" 
"新建文件后，自动定位到文件末尾 
autocmd BufNewFile * normal G
"定义函数SetTitle，自动插入文件头 
func SetTitle()
""call setline(1, "//********************************************************************") 
""call append(0, "// Time: ".strftime("%c")) 
""call append(0, "// Description: ") 
""call append(0, "// File Name: ".expand("%")) 
if &filetype == 'cpp' 
call append(1, "#include <iostream>") 
call append(2, "using namespace std;") 
call append(3, "int main(void)") 
call append(4, "{ ") 
call append(5, "    return 0;")
call append(6, "}")
call append(5, " ")
call append(3, " ")
call append(2, " ")
elseif &filetype == 'c' 
call append(1, "#include <stdio.h>") 
call append(2, " ") 
call append(3, "int main()") 
call append(4, "{") 
call append(5, "    return 0;")
call append(6, "}") 
call append(5, " ") 
elseif &filetype == 'java' 
call append(1, "public class ".expand("%<").expand("{")) 
call append(2, "  public static void main(String[] args)") 
call append(3, "  {") 
call append(4, "       System.out.println();")
call append(5, "  }") 
call append(6, "}") 
call append(4, " ") 
call append(2, " ") 
elseif &filetype == 'python' 
call append(0,"# -*- coding: utf-8 -*-")
call append(1,"# !/usr/local/bin/python")
call append(2, "# Time: ".strftime("%c")) 
call append(3, "# Description:") 
call append(4, "# File Name: ".expand("%")) 
call append(5,"")
endif 
endfunc
"用空格键来开关折叠
set foldenable
set foldmethod=manual
nnoremap <space> @=((foldclosed(line('.')) < 0) ? 'zc':'zo')<CR>
"自动补全功能
set tags+=tags
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set guioptions-=m
set guioptions-=T
set guioptions-=L
"set guioptions-=r
set guioptions-=B
set guioptions-=e
set guioptions+=c
"map <silent> <F4> :if &guioptions =~# 'T' <Bar>
""winpos 450 235
set lines=33 columns=100
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"gvim打开以后最大化
au GUIEnter * simalt ~x
"when started as "evim",evim.vim will already have done these settings
if v:progname =~? "evim"
    finish
endif
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set smarttab
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"状态行颜色
""highlight StatusLine guifg=SlateBlue guibg=Yellow
""highlight StatusLineNC guifg=Gray guibg=White
"允许backspace和光标键跨越行边界
set whichwrap+=<,>,h,l
"保留正则表达式匹配的行"
function! KeepLines(pattern)
    let pattern = a:pattern
    let hits = []
    exec '%s/' . pattern . '/\=add(hits, submatch(0))/ge'
    let str = join(hits, "\n") . "\n"
    %d
    put! = str
endfunction
command! -nargs=1 KeepLines call KeepLines(<f-args>)
"split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
""以达到当剩余的窗口都不是文件编辑窗口时，自动退出vim
autocmd BufEnter * if 0 == len(filter(range(1, winnr('$')), 'empty(getbufvar(winbufnr(v:val), "&bt"))')) | qa! | endif
au BufNewFile,BufRead *.py,*.pyw setf python
set ofu=syntaxcomplete#Complete
autocmd FileType python setlocal omnifunc=pythoncomplete#Complete
autocmd FileType python runtime! autoload/pythoncomplete.vim


if has('multi_byte_ime')  
 "未开启IME时光标背景色  
 hi Cursor guifg=bg guibg=Orange gui=NONE  
 "开启IME时光标背景色  
 hi CursorIM guifg=NONE guibg=Skyblue gui=NONE  
 " 关闭Vim的自动切换IME输入法(插入模式和检索模式)  
 set iminsert=0 imsearch=0  
 " 插入模式输入法状态未被记录时，默认关闭IME  
 "inoremap <silent> <ESC> <ESC>:set iminsert=0<CR>  
endif  


let $PYTHONUNBUFFERED=1
source $VIMRUNTIME/delmenu.vim 
source $VIMRUNTIME/menu.vim 
