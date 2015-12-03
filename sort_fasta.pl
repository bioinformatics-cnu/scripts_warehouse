#written by thippo
#2015.10.31

#sort fasta file with length of the sequences

open(FILE,'input_file.fasta');
open(OUT,'>output_file.out');
while(<FILE>){
chomp;
if ($_=~m/>/){
$name=$_;
$hash_fasta{$name}='';
}else{
$hash_fasta{$name}.=$_;}}
foreach(keys %hash_fasta){
$hash_len{$_}=length($hash_fasta{$_});}
foreach(sort {$hash_len{$b} <=> $hash_len{$a} } keys %hash_len){
print OUT "$_\n$hash_fasta{$_}\n"}
close(FILE);
close(OUT);