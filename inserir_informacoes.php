<?php
#inserir informações

$nome = "victor";
$telefone = "123456";

$sql = "INSERT INTO bot (nome, telefone) VALUES ('$nome', '$telefone')";
$query = mysqli_query($conn, $sql);

if(!$query){
    echo "erro ao inserir";
} else{
    echo "inserido com sucesso";
}
?>