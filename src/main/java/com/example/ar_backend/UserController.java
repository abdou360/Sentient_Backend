package com.example.ar_backend;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/users")
public class UserController {
    @Autowired
    UserRepository userRepository;
    @GetMapping()
    ResponseEntity<List<UserEntity>> getAllUsers(){
        List<UserEntity> allUsers = userRepository.findAll();
    return new ResponseEntity<List<UserEntity>>( allUsers, HttpStatus.OK);

    }
    @PostMapping()
    ResponseEntity<UserEntity> setOneUsers(@RequestBody UserResuest user){
        UserEntity userEntity1 = new UserEntity();
        userEntity1.setName(user.getName());
        UserEntity userEntity = userRepository.save(userEntity1);

        return new ResponseEntity<UserEntity>( userEntity, HttpStatus.CREATED);
    }

}

