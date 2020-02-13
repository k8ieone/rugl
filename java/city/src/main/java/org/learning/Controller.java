package org.learning;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.learning.WebApp;

@RestController
public class Controller {

    @RequestMapping("/")
    public String index(){
        return "Henlo";
    }
}
