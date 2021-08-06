var app = new Vue({
    el: '#app',
    delimiters:['{$','$}'],
    data: {
      saludo: 'Hello Vue!',
      val: 'Esto es una prueba',
      contador:5
    },
    methods:{


      del:function(id,num){

        Swal.fire({
          title: '¿Estás seguro?',
          text: "estos cambios no seran reversibles!",
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Si, borrar!',
          cancelButtonText:"Cancelar"
        }).then((result) => {
          if (result.isConfirmed) {
            if (num==2){
              window.location.href=`http://209.90.232.169:8081/inventario/libroDelete/${id}`;

            }else{

              window.location.href=`http://209.90.232.169:8081/inventario/autorDelete/${id}`;
            }

            

            Swal.fire(
              'Eliminado!',
              'Los archivos han sido eliminados.',
              'success'
            ) 
          }
        })
        //console.log("Se presiono el boton eliminar");

      },

      form:()=>{

        console.log("Agregar un nuevo usuario");
        $('#modalForm').modal('show');

        

      }
    }
  })