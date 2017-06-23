// *******************************************************
// PARTIALLY GENERATED FILE -- Edit the indicated sections
// Parameterized with:
//
// EndpointName = index
// RequestName = dataPath
// RequestType = string
// ResponseName = status
// ResponseType = string
// ********************************************************

package main

import (
	"fmt"
	"os/exec"

	"github.com/prometheus/common/log"
)

type indexService interface {
	Callindex(string) (string, error)
}

type service struct{}

// Define the service output struct if not native type

func (service) Callindex(input string) (string, error) {

	var err error

	cmd := fmt.Sprintf("python", "-query", input)
	if exec.Command("sh", "-c", cmd).Run(); err != nil {
		log.Error(err)
		return "Failed indexing", err
	}

	return "", nil
}
