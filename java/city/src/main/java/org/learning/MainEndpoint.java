package org.learning;

import org.learning.configuration.NonResidentialBuildingsManagerBean;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Lazy;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.learning.WebApp;

@RestController
@RequestMapping("/main")
public class MainEndpoint {

    @Autowired
    @Lazy
    NonResidentialBuildingsManagerBean ins;

}
