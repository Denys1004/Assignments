$('form').submit(function(event){
    event.preventDefault();             // 1. First prevent default behavier
    var form = $(this);                 // 3. data will come from the form object, this refers to the form where event were fired from (if we ave many forms, this will be the one where submit button was clicked)
    // console.log(form.serialize());
    $.ajax({                            // 2. call AJAX function
        url: '/create',                 // 2a. where you want this form submition to go
        method: 'POST',                 // 2b. what type of request you want to make
        data: form.serialize()          // 2c. data from this form     4. If you submit you form now, you will see that you able to save data from here! 
    }).done(function(response){         // 5. function done will fire when you get response back (it will return whole html with data)
        $('tbody').html(response)       // 10. if we think of this response as html of rows, we can select it and set inner html to be response.
    })
})

// 6. we want to have stuff that you want to appear, and function that returns just those rows as html
// 7. Now go to html and cut the loop between <tbody> CUT from here data you want to show with ajax </tbody>
// 8. create new html (users.html) with what you've cut from <tbody> 
// 9. The idea is if we can take response from server(now its whole html), and if this response was just <tr>users</tr>, 
// select my tbody and SET inner html to be that renponse <tr>users</tr>.