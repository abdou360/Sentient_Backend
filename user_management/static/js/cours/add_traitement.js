var current_fs, next_fs, previous_fs; 
var left, opacity, scale; 
var animating;
var selectedValue;

$("input[type='radio'][name='radioGroup']").change(function() {
    selectedValue = $("input[type='radio'][name='radioGroup']:checked").val();
    // alert( "Handler for .change() called." + selectedValue );
});



$(".next-to-2").click(function(){
    if(animating) return false;
    animating = true;

    current_fs = $(this).parent();

    switch (selectedValue) {
        case "Image":
            next_fs = $("#fs-image")
            break;
        case "QR-Code":
            next_fs = $("#fs-qrcode")
            break;
        case "Texte":
            next_fs = $("#fs-texte")
            break;
        default:
            next_fs = $("#fs-image")
            break;
    }
    $("#li-second").addClass("active");
    next_fs.show(); 
    current_fs.animate({opacity: 0}, {
        step: function(now, mx) {
            scale = 1 - (1 - now) * 0.2;
            left = (now * 50)+"%";
            opacity = 1 - now;
            current_fs.css({
                'transform': 'scale('+scale+')',
                'position': 'absolute'
            });
            next_fs.css({'left': left, 'opacity': opacity});
        }, 
        duration: 800, 
        complete: function(){
            current_fs.hide();
            animating = false;
        }, 
        easing: 'easeInOutBack'
    });
});

$(".previous-to-1").click(function(){
    if(animating) return false;
    animating = true;
    current_fs = $(this).parent();
    previous_fs = $("#fs-1");
    $("#li-second").removeClass("active");
    previous_fs.show();
    current_fs.animate({opacity: 0}, {
        step: function(now, mx) {
            scale = 0.8 + (1 - now) * 0.2;
            left = ((1-now) * 50)+"%";
            opacity = 1 - now;
            current_fs.css({'left': left});
            previous_fs.css({'transform': 'scale('+scale+')', 'opacity': opacity});
        }, 
        duration: 800, 
        complete: function(){
            current_fs.hide();
            animating = false;
        },
        easing: 'easeInOutBack'
    });
});



$(".next-to-3").click(function(){
    if(animating) return false;
    animating = true;
    
    current_fs = $(this).parent();
    next_fs = $("#fs-3");
    $("#li-third").addClass("active");
    next_fs.show();
    current_fs.animate({opacity: 0}, {
        step: function(now, mx) {
            scale = 1 - (1 - now) * 0.2;
            left = (now * 50)+"%";
            opacity = 1 - now;
            current_fs.css({
                'transform': 'scale('+scale+')',
                'position': 'absolute'
            });
            next_fs.css({'left': left, 'opacity': opacity});
        }, 
        duration: 800, 
        complete: function(){
            current_fs.hide();
            animating = false;
        },
        easing: 'easeInOutBack'
    });
});

$(".previous-to-2").click(function(){
    if(animating) return false;
    animating = true;
    current_fs = $(this).parent();
    switch (selectedValue) {
        case "Image":
            previous_fs = $("#fs-image")
            break;
        case "QR-Code":
            previous_fs = $("#fs-qrcode")
            break;
        case "Texte":
            previous_fs = $("#fs-texte")
            break;
        default:
            previous_fs = $("#fs-image")
            break;
    }
    $("#li-third").removeClass("active");
    previous_fs.show();
    current_fs.animate({opacity: 0}, {
        step: function(now, mx) {
            scale = 0.8 + (1 - now) * 0.2;
            left = ((1-now) * 50)+"%";
            opacity = 1 - now;
            current_fs.css({'left': left});
            previous_fs.css({'transform': 'scale('+scale+')', 'opacity': opacity});
        }, 
        duration: 800, 
        complete: function(){
            current_fs.hide();
            animating = false;
        }, 
        easing: 'easeInOutBack'
    });
});