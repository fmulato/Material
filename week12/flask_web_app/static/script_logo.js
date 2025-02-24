document.getElementById('change_img').addEventListener('click', function() {
            var input = document.createElement('input');
            input.type = 'file';
            input.accept = 'image/*';
            input.onchange = function(event) {
                var file = event.target.files[0];
                if (file) {
                    var reader = new FileReader();
                    reader.onload = function(e) {
                        document.getElementById('myimage').src = e.target.result;
                    }
                    reader.readAsDataURL(file);
                }
            };
            input.click();
        });
