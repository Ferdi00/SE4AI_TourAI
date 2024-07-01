using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Smanager : MonoBehaviour
{

      // Nome della scena di destinazione
    public string sceneToLoad;


    // Metodo chiamato quando il bottone viene premuto
    public void Load()
    {
        // Carica la scena di destinazione
        SceneManager.LoadScene(sceneToLoad);
    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
