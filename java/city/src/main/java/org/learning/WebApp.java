package org.learning;


import org.learning.configuration.NonResidentialBuildingsManagerBean;
import org.learning.managers.NonResidentialBuildingsManagerImplementation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class WebApp {

    public static void main(String[] args){

        SpringApplication.run(WebApp.class, args);

    }

}
