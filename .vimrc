" disable arrow keys
noremap <Up> <Nop>
noremap <Down> <Nop>
noremap <Left> <Nop>
noremap <Right> <Nop>
noremap <Backspace> <Nop>

" " Scroll with mouse
set mouse=a

" Turn on syntax highlighting
syntax enable 

" Show line numbers
set number

" Don't make vi compatible
set nocompatible

" Automatic paste toggle for tmux+vim
function! WrapForTmux(s)
if !exists('$TMUX')
return a:s
endif

let tmux_start = "\<Esc>Ptmux;"
let tmux_end = "\<Esc>\\"

return tmux_start . substitute(a:s, "\<Esc>", "\<Esc>\<Esc>", 'g') . tmux_end
endfunction

let &t_SI .= WrapForTmux("\<Esc>[?2004h")
let &t_EI .= WrapForTmux("\<Esc>[?2004l")

function! XTermPasteBegin()
set pastetoggle=<Esc>[201~
set paste
return ""
endfunction

inoremap <special> <expr> <Esc>[200~ XTermPasteBegin() 

noremap <leader>u :w<Home>silent <End> !urlview<CR>

"" Vimwiki instant markdown
  "Uncomment to override defaults:
 let g:instant_markdown_port = 8080
let g:instant_markdown_browser = "icecat --new-window"
 let g:instant_markdown_autostart = 0    " disable autostart
 map <leader>md :InstantMarkdownPreview<CR>"
 
 let g:vimwiki_list = [{'path': '~/vimwiki/',
                       \ 'syntax': 'markdown', 'ext': '.md'}]
